# FastAPI service patterns

Loaded by `/python fastapi`. The shape of a service worth shipping.

## FastAPI (`/python fastapi`)

Production-oriented patterns for FastAPI services. Treat FastAPI as a thin HTTP layer over explicit dependencies and service code.

### Architecture

- `main.py` — app construction, middleware, exception handlers, router registration
- `schemas/` — Pydantic request and response models
- `dependencies.py` — database, auth, pagination, request-scoped dependencies
- `services/` or `crud/` — business and persistence operations
- `tests/` — override dependencies instead of opening production resources

### Project Layout

```
app/
├── main.py
├── config.py
├── dependencies.py
├── exceptions.py
├── api/routes/
│   ├── users.py
│   └── health.py
├── core/
│   ├── security.py
│   └── middleware.py
├── db/
│   ├── session.py
│   └── crud.py
├── models/
├── schemas/
└── tests/
```

### Application Factory

Use a factory so tests and workers can build the app with controlled settings.

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()

def create_app() -> FastAPI:
    app = FastAPI(title=settings.api_title, version=settings.api_version, lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=bool(settings.cors_origins),  # never True with ["*"]
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
        allow_headers=["Authorization", "Content-Type"],
    )
    register_exception_handlers(app)
    app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
    return app

app = create_app()
```

Do NOT use `allow_origins=["*"]` with `allow_credentials=True` — browsers reject it.

### Pydantic Schemas

Keep request, update, and response models separate. Response models must never include password hashes, tokens, or internal auth state.

```python
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Annotated
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    full_name: Annotated[str, Field(min_length=1, max_length=100)]

class UserCreate(UserBase):
    password: Annotated[str, Field(min_length=12, max_length=128)]

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    full_name: Annotated[str | None, Field(min_length=1, max_length=100)] = None

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    created_at: datetime
    updated_at: datetime
```

### Dependency Injection

Use dependency injection for request-scoped resources. Never create sessions, clients, or credentials inline inside route handlers.

```python
async def get_db() -> AsyncIterator[AsyncSession]:
    async with session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    payload = decode_token(token)
    user = await db.get(User, UUID(payload["sub"]))
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user
```

### Async Endpoints

Keep route handlers async when they perform I/O. Use `httpx.AsyncClient` for external calls — never `requests` inside an async route.

```python
@router.get("/", response_model=list[UserResponse])
async def list_users(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(User).order_by(User.created_at.desc()).limit(limit).offset(offset)
    )
    return result.scalars().all()
```

### Error Handling

```python
class ApiError(Exception):
    def __init__(self, status_code: int, code: str, message: str):
        self.status_code = status_code
        self.code = code
        self.message = message

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(ApiError)
    async def handler(request: Request, exc: ApiError):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": {"code": exc.code, "message": exc.message}},
        )
```

### Testing

Override the dependency used by `Depends`, not an internal helper that route handlers never reference.

```python
@pytest.fixture
async def client(test_session: AsyncSession):
    app = create_app()

    async def override_get_db():
        yield test_session

    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()
```

### Security Checklist

- Hash passwords with `argon2-cffi`, `bcrypt`, or current passlib hasher
- Validate JWT issuer, audience, expiry, and signing algorithm
- Keep CORS origins environment-specific (not hardcoded `["*"]`)
- Rate-limit auth and write-heavy endpoints
- Use Pydantic models for all request bodies — never raw dicts
- ORM parameter binding or SQLAlchemy Core expressions — never f-string SQL
- Redact tokens, auth headers, cookies, and passwords from logs
- Run `pip-audit` and `bandit` in CI

### Performance Checklist

- Configure DB connection pooling explicitly
- Paginate all list endpoints
- Watch for N+1 queries; use eager loading intentionally
- Async HTTP/DB clients in async paths
- Cache stable expensive reads with explicit invalidation
