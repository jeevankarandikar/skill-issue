---
name: python
description: Python development patterns and FastAPI production patterns. Use when building, reviewing, or debugging Python code. Covers Pythonic idioms, type hints, error handling, async patterns, dataclasses, and package organization. Invoke with 'fastapi' for FastAPI-specific patterns.
version: 2.0.0
user-invocable: true
argument-hint: "[fastapi]"
---

# Python

Core Python patterns and FastAPI production patterns in one skill.

| Mode | What it does |
|---|---|
| `/python` | Core Python: idioms, type hints, error handling, concurrency, package layout |
| `/python fastapi` | FastAPI: app factory, schemas, DI, async endpoints, testing, security |

---

## Core Python

### Principles

**Readability counts — prefer obvious over clever:**
```python
# Good
def get_active_users(users: list[User]) -> list[User]:
    return [user for user in users if user.is_active]

# Bad
def get_active_users(u): return [x for x in u if x.a]
```

**EAFP over LBYL:**
```python
# Good — catch and handle
def get_value(d: dict, key: str) -> Any:
    try:
        return d[key]
    except KeyError:
        return default_value

# Bad — check first
def get_value(d: dict, key: str) -> Any:
    if key in d:
        return d[key]
    return default_value
```

### Type Hints

```python
# Python 3.9+ — use built-in types
def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# Union and Optional (Python 3.10+ syntax)
def find_user(user_id: str) -> User | None: ...

# TypeVar for generics
T = TypeVar('T')
def first(items: list[T]) -> T | None:
    return items[0] if items else None

# Protocol-based duck typing
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str: ...

def render_all(items: list[Renderable]) -> str:
    return "\n".join(item.render() for item in items)
```

### Error Handling

```python
# Specific exceptions + chaining
def load_config(path: str) -> Config:
    try:
        with open(path) as f:
            return Config.from_json(f.read())
    except FileNotFoundError as e:
        raise ConfigError(f"Config file not found: {path}") from e
    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON in config: {path}") from e

# Custom exception hierarchy
class AppError(Exception): pass
class ValidationError(AppError): pass
class NotFoundError(AppError): pass
```

**Never use bare `except:` or `except Exception: pass`.** Every caught exception either retries, degrades gracefully, or re-raises with context.

### Context Managers

```python
# Use with for resource management
def process_file(path: str) -> str:
    with open(path) as f:
        return f.read()

# Custom context manager
from contextlib import contextmanager

@contextmanager
def timer(name: str):
    start = time.perf_counter()
    yield
    print(f"{name}: {time.perf_counter() - start:.4f}s")
```

### Comprehensions and Generators

```python
# List comprehension for simple transforms
names = [user.name for user in users if user.is_active]

# Generator for lazy eval / large data
total = sum(x * x for x in range(1_000_000))

# Generator function
def read_large_file(path: str) -> Iterator[str]:
    with open(path) as f:
        for line in f:
            yield line.strip()
```

Complex comprehensions with multiple conditions should be expanded into a generator function.

### Data Classes

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class User:
    id: str
    name: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)
    is_active: bool = True

    def __post_init__(self):
        if "@" not in self.email:
            raise ValueError(f"Invalid email: {self.email}")
```

Use `NamedTuple` for immutable data:
```python
class Point(NamedTuple):
    x: float
    y: float

    def distance(self, other: 'Point') -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
```

### Decorators

```python
import functools

def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

# Parameterized
def repeat(times: int):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator
```

### Concurrency

```python
# I/O-bound — threads
import concurrent.futures

def fetch_all_urls(urls: list[str]) -> dict[str, str]:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(fetch_url, url): url for url in urls}
        return {
            future_to_url[f]: f.result()
            for f in concurrent.futures.as_completed(future_to_url)
        }

# CPU-bound — processes
def process_all(datasets: list[list[int]]) -> list[int]:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        return list(executor.map(process_data, datasets))

# Async I/O
async def fetch_all(urls: list[str]) -> dict[str, str]:
    tasks = [fetch_async(url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return dict(zip(urls, results))
```

### Package Layout

```
myproject/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── main.py
│       ├── api/
│       ├── models/
│       └── utils/
├── tests/
│   ├── conftest.py
│   └── test_*.py
├── pyproject.toml
└── README.md
```

Import order: stdlib → third-party → local, each group separated by blank line.

### Performance

- `__slots__` for memory-efficient classes with many instances
- Generators over list comprehensions when the result isn't indexed
- `"".join(...)` instead of `+=` in loops (avoids O(n²) string copies)
- `pathlib.Path` over `os.path` string concatenation

### Tooling

```bash
black .          # format
isort .          # sort imports
ruff check .     # lint
mypy .           # type check
pytest --cov=mypackage
bandit -r .      # security scan
pip-audit        # dependency audit
```

### Anti-Patterns

```python
# BAD: mutable default argument
def append_to(item, items=[]):  # items is shared across calls!
    items.append(item)
    return items

# GOOD
def append_to(item, items=None):
    if items is None: items = []
    items.append(item)
    return items

# BAD: type() check
if type(obj) == list: ...
# GOOD: isinstance
if isinstance(obj, list): ...

# BAD: compare to None with ==
if value == None: ...
# GOOD
if value is None: ...

# BAD: wildcard import
from os.path import *
# GOOD: explicit
from os.path import join, exists

# BAD: bare except
try:
    risky()
except:
    pass
# GOOD: specific
try:
    risky()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
```

---

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
