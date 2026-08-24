# Asset Generation (`/design assets`)

Generate brand assets — **codegen-first**. Most assets are structural and should be produced *deterministically* (same input → same output), not hallucinated by an image model. Even most logos are code (wordmarks, geometric marks) — author them as SVG with the model already running. For the rare *illustrative* mark, hand the user a tailored prompt for whatever image tool they already use — no key, no integration.

| Asset | Tool | Output | Cost |
|---|---|---|---|
| **OG / social image** | satori + resvg (or `@vercel/og` in Next) | SVG→PNG | **free**, deterministic |
| **Icon set** | Iconify API (Lucide / Phosphor / …) | SVG | **free** |
| **Favicon set** | `pwa-asset-generator` / `@realfavicongenerator/cli` | ICO + PNG + markup | **free**, local |
| **Logo mark** | running model → SVG (wordmark/geometric); paste-ready prompt for the user's image tool (illustrative) | SVG / their tool | **free — no key** |

Nothing here needs a key. The structural assets are codegen; logos are either SVG authored by the model already running, or — for illustrative marks — a ready-to-paste prompt for whatever image tool the user already has (see below).

## OG / social images — `scripts/assets/generate-og.mjs`

A deterministic 1200×630 image from your DESIGN.md tokens. No model, no hallucination, reproducible, versionable.

- **Standalone:** `npm i satori satori-html @resvg/resvg-js`, supply TTF/OTF fonts, then `node scripts/assets/generate-og.mjs "Headline" "Subtitle"`.
- **In a Next.js app:** prefer `@vercel/og`'s `ImageResponse` in an `opengraph-image.tsx` route (same engine, edge-rendered).
- Edit the brand tokens at the top of the script to match DESIGN.md. **satori does not support OKLCH** — convert tokens to hex for this one file.

## Icon sets — `scripts/assets/assemble-icons.mjs`

Assemble a curated, consistent set from Iconify's ~200k open-source icons (Lucide, Phosphor, Heroicons, Tabler…). Curated assembly beats per-icon model generation — consistent stroke/style, free, license-clean, instant.

```
node scripts/assets/assemble-icons.mjs --out ./src/icons --color "#18181b" lucide:home lucide:search ph:gear-six
node scripts/assets/assemble-icons.mjs --out ./src/icons --sprite icons.svg lucide:home lucide:user
```

Browse ids at icon-sets.iconify.design. Favor ONE family (defaults: Lucide or Phosphor) — never mix families in one UI. Pipe through SVGO if installed for smaller output.

## Favicons — CLI, no key

From a single source image (your logo SVG/PNG):

```
npx pwa-asset-generator ./logo.svg ./public/icons --favicon --opaque false
# or a full favicon set + <link> markup:
npx @realfavicongenerator/cli ./logo.svg ./public
```

Generates the multi-size favicon set + Apple/PWA icons + the markup. Deterministic, local.

## Logo mark — free, no key

Two paths, both keyless:

**1. Wordmark or geometric / monogram mark → the running model authors SVG.** The default. Typeset the name (per [typography.md](typography.md)) or draw clean SVG paths and shapes directly — the same path used for icons. Vector, editable, on-brand, instant.

**2. Illustrative / painterly mark → hand over a tailored prompt.** When the brief genuinely needs an illustrated mark (a mascot, a crest, a textured emblem) that can't be authored as code, don't wire up an API — **generate a ready-to-paste image-gen prompt** the user drops into whatever image tool they already have (ChatGPT / GPT-image, Gemini, Midjourney, Ideogram, Recraft). Build it from DESIGN.md:

> **`[Brand]` logo — a `[symbol / monogram / emblem]` of `[motif]`. `[3 brand-voice adjectives]`. Flat vector style, solid `[brand color]`, centered, simple and memorable, legible down to a favicon. Transparent background. No text, no gradients, no photorealism, no drop shadows, no 3D.**

Tailor per tool: **Ideogram / GPT-image** if the mark contains lettering · **Recraft** (`vector` style) when they want true SVG out · **Midjourney** add `--no text gradient photorealism`. Tell them to request an SVG or a transparent PNG, and to iterate on the *prompt*, not the picture.

**Optional automation:** if the user has a key and wants it generated in-pipeline, `RECRAFT_API_KEY` (true SVG + transparency) or `GEMINI_API_KEY` (raster). Opt-in convenience — never required.

---

**Avoid**: using an image model for OG/favicon/icons (codegen is deterministic, free, on-brand) · reaching for an image model when an SVG the running model can author would do · wiring up an API key when a paste-ready prompt for the user's existing image tool is simpler · mixing icon families in one UI · OKLCH in satori (unsupported — hex for the OG file only).
