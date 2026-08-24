// generate-og.mjs — generate a 1200x630 OG/social image from your design tokens, no model.
// deterministic codegen: satori (HTML -> SVG) + resvg (SVG -> PNG). reproducible + versionable.
//
// deps:   npm i satori satori-html @resvg/resvg-js
// fonts:  satori needs TTF/OTF (NOT woff2). download e.g. Geist from github.com/vercel/geist-font
//         and point OG_FONT_BOLD / OG_FONT_REGULAR at the .ttf files (or edit the defaults below).
// usage:  node generate-og.mjs "Your headline" "Optional subtitle" --out og.png

import satori from "satori";
import { html } from "satori-html";
import { Resvg } from "@resvg/resvg-js";
import { readFile, writeFile } from "node:fs/promises";

const argv = process.argv.slice(2);
const outIdx = argv.indexOf("--out");
const out = outIdx !== -1 ? argv[outIdx + 1] : "og.png";
const positional = argv.filter((a, i) => !a.startsWith("--") && argv[i - 1] !== "--out");
const [title = "Untitled", subtitle = ""] = positional;

// --- brand tokens: edit to match DESIGN.md. satori has NO OKLCH support -> use hex. ---
const BG = "#101014", FG = "#f4f4f5", ACCENT = "#34d3c0", MUTED = "#9b9ba3";

const bold = await readFile(process.env.OG_FONT_BOLD || "./fonts/Geist-Bold.ttf");
const regular = await readFile(process.env.OG_FONT_REGULAR || "./fonts/Geist-Regular.ttf");

const markup = html`
  <div style="height:100%;width:100%;display:flex;flex-direction:column;justify-content:space-between;background:${BG};color:${FG};padding:80px;font-family:Brand">
    <div style="display:flex;align-items:center;color:${ACCENT};font-size:28px;font-weight:700">yourbrand</div>
    <div style="display:flex;flex-direction:column">
      <div style="font-size:64px;font-weight:700;line-height:1.05;letter-spacing:-0.03em">${title}</div>
      ${subtitle ? `<div style="font-size:30px;color:${MUTED};margin-top:16px">${subtitle}</div>` : ""}
    </div>
    <div style="font-size:22px;color:${MUTED}">yourbrand.com</div>
  </div>`;

const svg = await satori(markup, {
  width: 1200,
  height: 630,
  fonts: [
    { name: "Brand", data: bold, weight: 700, style: "normal" },
    { name: "Brand", data: regular, weight: 400, style: "normal" },
  ],
});

const png = new Resvg(svg).render().asPng();
await writeFile(out, png);
console.log(`OK  ${out}  (1200x630)`);
