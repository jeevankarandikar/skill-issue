# `/check optimize` — patterns and snippets

### Baseline First

```bash
# Lighthouse CI
npx lighthouse https://your-app.com --output=json --output-path=baseline.json

# Bundle analysis
npx source-map-explorer 'build/static/js/*.js'
# or for Next.js:
ANALYZE=true npm run build
```

### Fixing Core Web Vitals

**Fixing LCP**: serve images via CDN, preload hero image (`<link rel="preload">`), inline critical CSS above the fold.

**Fixing INP**: break long tasks (> 50ms) with `scheduler.yield()` or `setTimeout(0)`, move heavy work to Web Workers.

**Fixing CLS**: `aspect-ratio` on images/video, reserve space for dynamic content (ads, embeds), `font-display: swap` + preload fonts.

```css
/* CLS prevention for images */
.hero-image {
  aspect-ratio: 16 / 9;
  width: 100%;
  height: auto;
}
```

### Images

```html
<!-- Modern formats with srcset -->
<picture>
  <source type="image/avif" srcset="hero.avif 1x, hero@2x.avif 2x">
  <source type="image/webp" srcset="hero.webp 1x, hero@2x.webp 2x">
  <img src="hero.jpg" alt="..." loading="lazy" decoding="async"
       width="800" height="450">
</picture>
```

- Lazy load everything below the fold: `loading="lazy"`
- `decoding="async"` on all images
- Serve via CDN with proper cache headers
- WebP for photos, SVG for icons/illustrations

### JavaScript Bundle

```js
// Route-based code splitting
const HeavyPage = lazy(() => import('./HeavyPage'));

// Dynamic imports for large deps
const { parse } = await import('date-fns');

// Tree shaking: named imports only
import { format } from 'date-fns'; // good — not import * as dateFns
```

- Run `npm ls` to find duplicate dependencies
- `npm dedupe` to consolidate
- Remove unused deps: `npx depcheck`

### CSS

```html
<!-- Critical CSS inline, rest deferred -->
<style>/* above-the-fold styles */</style>
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

CSS containment for complex components:
```css
.card { contain: layout style; }
.independent-widget { contain: strict; }
```

### Fonts

```css
@font-face {
  font-display: swap;           /* show fallback immediately */
  unicode-range: U+0000-00FF;   /* subset to Latin characters */
}
```

Preload critical fonts:
```html
<link rel="preload" href="/fonts/heading.woff2" as="font" type="font/woff2" crossorigin>
```

### Rendering

Batch DOM reads and writes — never interleave:

```js
// BAD: layout thrashing
elements.forEach(el => el.style.height = el.offsetHeight + 'px');

// GOOD: batch reads then writes
const heights = elements.map(el => el.offsetHeight); // all reads first
elements.forEach((el, i) => el.style.height = heights[i] + 'px'); // then all writes
```

`content-visibility: auto` for long scrolling lists:
```css
.list-item { content-visibility: auto; contain-intrinsic-size: 0 64px; }
```

Virtual scrolling for lists > 500 items (use `@tanstack/virtual` or `react-virtuoso`).

### Animations

```css
/* Animate ONLY transform and opacity — never layout properties */
/* BAD: triggers full repaint */
.bad { transition: width 300ms, height 300ms, top 300ms; }

/* GOOD: GPU-composited */
.good { transition: transform 300ms, opacity 300ms; }
```

Use `will-change: transform` right before an animation starts; remove it after:

```js
element.addEventListener('mouseenter', () => element.style.willChange = 'transform');
element.addEventListener('mouseleave', () => element.style.willChange = 'auto');
```

Use `IntersectionObserver` for scroll-triggered effects, never `window.addEventListener('scroll')`.

### React

```jsx
// Memoize expensive renders
const HeavyList = React.memo(({ items }) => (
  <ul>{items.map(item => <Item key={item.id} {...item} />)}</ul>
));

// Stable callbacks
const handleClick = useCallback((id) => removeItem(id), [removeItem]);

// Memoize derived data
const sortedItems = useMemo(() => [...items].sort(compareFn), [items]);
```

Avoid anonymous functions in JSX renders — creates new reference on every render.
