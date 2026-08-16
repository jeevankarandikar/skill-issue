# Web Implementation

Design *in* the web stack — Tailwind v4 + shadcn/ui + Next App Router. The taste rules (OKLCH, dials, anti-slop bans) live in the main skill and the other references; this is how they land in code.

## Tailwind CSS v4

v4 is CSS-first and OKLCH-native — which validates the color stance in [color-and-contrast.md](../color-and-contrast.md).

- **Config lives in CSS** via `@theme { }`. Tokens defined there become BOTH utilities and runtime CSS variables — one source of truth.
```css
@theme {
  --color-canvas: oklch(0.99 0.003 95);
  --color-accent: oklch(0.62 0.17 25);
  --font-display: "Your Display Face", sans-serif;
}
```
- Default palette is OKLCH (wider gamut, perceptually uniform). Define custom tokens the same way: `--color-x: oklch(L C H)`.
- Setup: `@tailwindcss/postcss` or the Vite plugin. Do NOT use the v3 `tailwindcss` PostCSS plugin on a v4 project.

## When the brief matches an official design system

Reach for the real system instead of imitating its look with Tailwind — one design system and one icon family per project:

| Brief reads as… | Use |
|---|---|
| Microsoft / enterprise | `@fluentui/react-components` |
| Material-flavored | `@material/web` + Material 3 tokens |
| IBM-style B2B analytics | `@carbon/react` + `@carbon/styles` |
| Atlassian / Jira-style | `@atlaskit/*` + `@atlaskit/tokens` |
| GitHub devtool / community | `@primer/css` or `@primer/react-brand` |
| Public-sector UK | `govuk-frontend` |
| US public-sector / trust-first | `uswds` |
| Modern accessible foundation | `@radix-ui/themes` |
| Modern SaaS, owned components | shadcn/ui |

## shadcn/ui

The right substrate *if you then make it yours* — shipping raw shadcn defaults is how the monoculture spreads.

- Install via CLI (`npx shadcn@latest add <component>`); run `init` first. Never hand-copy component source.
- **Theme via CSS variables** in `:root` + `.dark`, semantic names (`--primary` / `--primary-foreground`), referenced as `bg-primary text-primary-foreground` — never hardcoded `bg-blue-500 text-white`.
- Compose with compound components (`Card` → `CardHeader` → `CardContent`) and `cva` variants; customize via `className`. Don't edit vendored source — but DO override the look (color, radius, density, motion) so it doesn't read as default shadcn.

## Next.js App Router

- **Server Components by default.** Push `'use client'` down to the leaf interactive nodes — never the whole tree.
- **Stream with `<Suspense>`**; add `loading.tsx` / `error.tsx` per route so loading and error states are design-consistent, not afterthoughts.
- `next/image` with explicit width+height (prevents layout shift), `priority` on the LCP/hero image. `next/font` with variable fonts set on `<body>` in the root layout (self-hosted, no FOUT).
- **Next 15+ `fetch` defaults to uncached** — set `cache: 'force-cache'` explicitly when you want caching.

---

**Avoid**: shipping default shadcn unchanged · hardcoded colors over semantic tokens · `'use client'` at the tree root · images without dimensions · the v3 PostCSS plugin on a v4 project. Sources: tailwindcss.com (v4), ui.shadcn.com, nextjs.org App Router docs.
