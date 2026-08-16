---
name: html-default-style
description: Default house style and technical baseline for generating HTML when the request does not name a visual style, framework, or specific HTML/CSS requirements. Produces a self-contained, accessible, responsive, light-and-dark, print-friendly page with tasteful neutral design tokens and none of the usual AI-generated clichés. If the user specifies a style, framework, brand, or particular technical requirement, follow that instead of this.
---

# Default HTML style

When you are asked to produce HTML and given no style direction, build a clean,
self-contained page that reads as considered, native software rather than a
template. Favor restraint over decoration. If the user names a framework, brand,
look, or specific technical requirement, follow that and ignore this skill.

## Technical baseline (always)

- One self-contained file. Put CSS in a single `<style>` block. Add inline
  JavaScript only when the page genuinely needs behavior; prefer none. No build step.
- No external requests. No CDN, no downloaded webfonts (Google Fonts, Font Awesome),
  no framework (Tailwind, Bootstrap, React, jQuery), no remote images. Embed any
  image as a data URI.
- Valid HTML5: `<!DOCTYPE html>`, `<html lang>`, `<meta charset="utf-8">`, a
  viewport meta tag, and a real `<title>`.
- Use the system font stack so the page loads instantly and looks native.
- Support light and dark with `prefers-color-scheme`, driven by CSS custom properties.
- Responsive: one centered content column with a max width, fluid padding with
  `clamp()`, holds up from phone to desktop.
- Accessible: semantic elements (`header`, `nav`, `main`, `section`, `table`, `ul`,
  `ol`, `figure`), a visible `:focus-visible` outline, `prefers-reduced-motion`
  honored, alt text on images, and color never the only signal.
- Print-friendly: include an `@media print` block and keep key blocks from breaking
  across pages.

## The default look (design tokens)

- Neutral, ink on white in light mode, inverted in dark. Near-black body text, muted
  secondary and tertiary grays, hairline borders, very subtle fills.
- Type: system sans. Cap font weight at 600, no 700 to 900 headline walls. Tighten
  letter-spacing as size grows. Body line-height around 1.47. Use tabular figures for
  numbers.
- Use semantic color (green, amber, red, or a single accent) sparingly, and always
  pair it with a word or label. Color is an accent, never a background decoration.
- Keep a consistent spacing rhythm and use hairline rules to separate sections.

Start from the block at the end, then add only the components the content needs.

## Forbidden (these read as AI slop)

- Colored left-border callout or admonition boxes. Use a plain hairline box and let
  the label word carry the meaning.
- Emoji in headings, labels, buttons, or as bullets or decoration.
- Gratuitous gradients (especially purple or indigo hero gradients), glassmorphism
  blur, and drop shadows on everything.
- Giant colored headline type as the only signal. State it in ink and keep color a
  small accent.
- CDN or webfont links, framework or icon-font includes, analytics, cookie banners,
  fake navigation, and invented logos.
- Lorem ipsum or fake placeholder charts unless the user asks for them.
- `!important` spam, deep absolute-positioning hacks where normal flow works, and
  inline `style=""` soup.
- Center-aligned body text, and full-viewport-width text with no measure.
- Exclamation marks and marketing tone in interface copy, ALL CAPS for emphasis, and
  em dashes.

## Expected-results checklist (objective rubric)

Score the output pass or fail on each item. Ship only when all pass.

1. Single file, valid HTML5, with doctype, `lang`, charset, viewport, and a title.
2. Zero external requests: no CDN, webfont, framework, icon font, or remote image.
3. CSS custom properties define the palette, and a complete `prefers-color-scheme`
   dark block exists.
4. Content sits in a centered, max-width column with fluid padding, and the layout
   holds on a narrow screen.
5. System font stack, no downloaded fonts, and weights do not exceed 600.
6. Semantic elements are used, a visible focus style exists, reduced motion is
   honored, and images have alt text.
7. An `@media print` block exists.
8. No forbidden clichés: no colored callout rails, no emoji decoration, no gratuitous
   gradient, blur, or shadow.
9. Color is paired with a word wherever it carries meaning, and nothing relies on
   color alone.
10. No em dashes, no ALL CAPS emphasis, and interface copy is plain and calm.

## Starter block (copy, then extend)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Document title</title>
<style>
  :root {
    --bg: #ffffff; --bg-elevated: #fbfbfd;
    --text: #1d1d1f; --text-second: #6e6e73; --text-third: #86868b;
    --hairline: #d2d2d7; --hairline-soft: rgba(0,0,0,0.07);
    --fill: rgba(0,0,0,0.028); --fill-strong: rgba(0,0,0,0.05);
    --accent: #0066cc; --focus: #0071e3;
    --clear: #1d8a34; --minor: #9a6700; --issues: #c8102e;
    --sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", system-ui, sans-serif;
    --mono: "SF Mono", SFMono-Regular, ui-monospace, Menlo, Consolas, monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #000000; --bg-elevated: #1c1c1e;
      --text: #f5f5f7; --text-second: #a1a1a6; --text-third: #86868b;
      --hairline: #424245; --hairline-soft: rgba(255,255,255,0.10);
      --fill: rgba(255,255,255,0.05); --fill-strong: rgba(255,255,255,0.09);
      --accent: #2997ff; --focus: #2997ff;
      --clear: #30d158; --minor: #ff9f0a; --issues: #ff453a;
    }
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: var(--sans); background: var(--bg); color: var(--text);
    font-size: 17px; line-height: 1.47059; letter-spacing: -0.022em;
    -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;
  }
  .wrap { max-width: 900px; margin: 0 auto; padding: 0 clamp(22px, 5vw, 40px); }
  a { color: var(--accent); text-decoration: none; }
  a:hover { text-decoration: underline; }
  :focus-visible { outline: 2px solid var(--focus); outline-offset: 3px; border-radius: 4px; }
  header.page { padding: clamp(44px, 8vh, 88px) 0 clamp(24px, 4vh, 44px); }
  header.page .eyebrow {
    font-size: 12px; font-weight: 600; letter-spacing: 0.055em;
    text-transform: uppercase; color: var(--text-third); margin-bottom: 16px;
  }
  h1 { font-size: clamp(32px, 5vw, 48px); font-weight: 600; line-height: 1.08; letter-spacing: -0.005em; }
  section.block { padding: clamp(32px, 5vh, 52px) 0; border-bottom: 1px solid var(--hairline); }
  section.block:last-of-type { border-bottom: none; }
  h2 { font-size: clamp(24px, 3vw, 32px); font-weight: 600; line-height: 1.12; margin-bottom: 12px; }
  p { max-width: 62ch; margin-bottom: 12px; color: var(--text); }
  table.data { width: 100%; border-collapse: collapse; font-size: 15px; }
  table.data th, table.data td {
    text-align: left; padding: 11px 14px; border-bottom: 1px solid var(--hairline-soft); vertical-align: top;
  }
  table.data th { font-weight: 400; color: var(--text-second); white-space: nowrap; width: 34%; }
  table.data td { font-variant-numeric: tabular-nums; }
  .note {
    margin: 16px 0; padding: 16px 18px; border: 1px solid var(--hairline);
    border-radius: 12px; background: var(--bg-elevated); font-size: 15.5px; line-height: 1.5;
  }
  .note .label {
    font-size: 12px; font-weight: 600; letter-spacing: 0.055em; text-transform: uppercase;
    color: var(--text-third); margin-bottom: 8px;
  }
  code { font-family: var(--mono); font-size: 0.86em; background: var(--fill-strong); padding: 2px 6px; border-radius: 5px; }
  pre {
    font-family: var(--mono); font-size: 13px; line-height: 1.55; background: var(--fill);
    border: 1px solid var(--hairline-soft); border-radius: 10px; padding: 14px 16px; overflow-x: auto; margin: 10px 0;
  }
  @media (prefers-reduced-motion: reduce) { * { transition: none !important; animation: none !important; } }
  @media print { section.block, header.page { break-inside: avoid-page; } }
</style>
</head>
<body>
  <header class="page">
    <div class="wrap">
      <div class="eyebrow">Section label</div>
      <h1>Document title</h1>
    </div>
  </header>
  <main class="wrap">
    <section class="block">
      <h2>Heading</h2>
      <p>Body text in a comfortable measure.</p>
    </section>
  </main>
</body>
</html>
```
