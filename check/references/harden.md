# `/check harden` — patterns and snippets

### Text Overflow & Wrapping

```css
/* Single line with ellipsis */
.truncate { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

/* Multi-line clamp */
.line-clamp {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Allow wrapping */
.wrap { word-wrap: break-word; overflow-wrap: break-word; hyphens: auto; }

/* Prevent flex/grid overflow */
.flex-item { min-width: 0; overflow: hidden; }
.grid-item { min-width: 0; min-height: 0; }
```

### Internationalization

**Text expansion**: Budget 30-40% for translations. Flexbox/grid that adapts to content. Avoid fixed widths on text containers.

```jsx
// ❌ Bad: assumes short English text
<button className="w-24">Submit</button>
// ✅ Good: adapts to content
<button className="px-4 py-2">Submit</button>
```

**RTL support** — use logical properties:
```css
margin-inline-start: 1rem;   /* not margin-left */
padding-inline: 1rem;         /* not padding-left/right */
border-inline-end: 1px solid; /* not border-right */
[dir="rtl"] .arrow { transform: scaleX(-1); }
```

**Date/number formatting**:
```javascript
new Intl.DateTimeFormat('en-US').format(date);  // 1/15/2024
new Intl.DateTimeFormat('de-DE').format(date);  // 15.1.2024
new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(1234.56);
// Use proper i18n library for pluralization — not manual `${count} item${count !== 1 ? 's' : ''}`
```

### Error Handling

**By HTTP status**:
- 400: Show validation errors inline
- 401: Redirect to login
- 403: Show permission error with explanation
- 404: Show not found state with navigation
- 429: Show rate limit message with retry timing
- 500: Generic error + support contact

**Patterns**: Inline errors near fields. Clear + specific messages. Suggest corrections. Preserve user input on error. Retry button for network failures.

**Graceful degradation**: Core functionality without JavaScript. Alt text on images. Progressive enhancement. Fallbacks for unsupported features.

### Edge Cases

**Empty states**: No items, no results, no notifications — provide clear next action.

**Loading states**: Initial load, pagination, refresh — show what's loading, time estimates for long ops.

**Large datasets**: Pagination or virtual scrolling. Search/filter. Don't load 10,000 items at once.

**Concurrent operations**: Disable button while loading (prevent double-submit). Handle race conditions. Optimistic updates with rollback.

**Permissions**: Clear explanation of why access is denied. Read-only mode states.

### Input Validation

```html
<input
  type="text"
  maxlength="100"
  pattern="[A-Za-z0-9]+"
  required
  aria-describedby="username-hint"
/>
<small id="username-hint">Letters and numbers only, up to 100 characters</small>
```

Client-side validation for UX. Server-side validation always (never trust client-side alone). Validate + sanitize. Rate limiting.

### Accessibility Resilience

Keyboard: all functionality accessible, logical tab order, focus management in modals, skip links.

Screen readers: proper ARIA labels, live regions for dynamic changes, semantic HTML.

```css
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

### Performance Resilience

**Slow connections**: Progressive image loading. Skeleton screens. Optimistic UI updates.

**Memory**: Clean up event listeners, cancel subscriptions, clear timers, abort pending requests on unmount.

**Debounce/throttle**:
```javascript
const debouncedSearch = debounce(handleSearch, 300);
const throttledScroll = throttle(handleScroll, 100);
```
