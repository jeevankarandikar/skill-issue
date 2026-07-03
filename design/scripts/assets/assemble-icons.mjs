#!/usr/bin/env node
// assemble-icons.mjs — assemble a curated icon set from the Iconify API (~200k free,
// open-source icons: Lucide, Phosphor, Heroicons, Tabler…). Writes normalized SVGs and
// an optional sprite. No build step, no deps — Node 18+ (native fetch).
//
// usage:
//   node assemble-icons.mjs --out ./src/icons --color "#18181b" --size 24 lucide:home ph:gear-six heroicons:bell
//   node assemble-icons.mjs --out ./src/icons --sprite icons.svg lucide:home lucide:search lucide:user
//
// icon ids are Iconify "prefix:name" — browse at https://icon-sets.iconify.design
// favor ONE family per UI (defaults: lucide or ph). don't mix.

import { mkdir, writeFile } from "node:fs/promises";
import { join } from "node:path";

const args = process.argv.slice(2);
const opt = { out: "./icons", color: "currentColor", size: null, sprite: null, names: [] };
for (let i = 0; i < args.length; i++) {
  const a = args[i];
  if (a === "--out") opt.out = args[++i];
  else if (a === "--color") opt.color = args[++i];
  else if (a === "--size") opt.size = args[++i];
  else if (a === "--sprite") opt.sprite = args[++i];
  else opt.names.push(a);
}
if (opt.names.length === 0) {
  console.error('no icons given. e.g. node assemble-icons.mjs --out ./icons lucide:home ph:gear-six');
  process.exit(1);
}

const q = new URLSearchParams();
if (opt.color && opt.color !== "currentColor") q.set("color", opt.color);
if (opt.size) { q.set("width", opt.size); q.set("height", opt.size); }
const qs = q.toString() ? `?${q}` : "";

await mkdir(opt.out, { recursive: true });

const fetched = [];
for (const id of opt.names) {
  const [prefix, name] = id.split(":");
  if (!prefix || !name) { console.warn(`skip "${id}" — expected prefix:name`); continue; }
  const url = `https://api.iconify.design/${prefix}/${name}.svg${qs}`;
  let res;
  try { res = await fetch(url); } catch (e) { console.warn(`skip "${id}" — ${e.message}`); continue; }
  if (!res.ok) { console.warn(`skip "${id}" — HTTP ${res.status}`); continue; }
  const svg = (await res.text()).trim();
  if (!svg.startsWith("<svg")) { console.warn(`skip "${id}" — not found in icon set`); continue; }
  const base = `${prefix}-${name}`;
  await writeFile(join(opt.out, `${base}.svg`), svg + "\n");
  fetched.push({ id, base, svg });
  console.log(`  ${id}  ->  ${base}.svg`);
}

if (opt.sprite && fetched.length) {
  const symbols = fetched.map(({ base, svg }) => {
    const viewBox = (svg.match(/viewBox="([^"]+)"/) || [, "0 0 24 24"])[1];
    const inner = svg.replace(/^<svg[^>]*>/, "").replace(/<\/svg>\s*$/, "");
    return `  <symbol id="${base}" viewBox="${viewBox}">${inner}</symbol>`;
  }).join("\n");
  const sprite = `<svg xmlns="http://www.w3.org/2000/svg" style="display:none">\n${symbols}\n</svg>\n`;
  await writeFile(join(opt.out, opt.sprite), sprite);
  console.log(`  sprite  ->  ${opt.sprite}   (use: <svg><use href="#${fetched[0].base}"/></svg>)`);
}

console.log(`\ndone — ${fetched.length}/${opt.names.length} icons in ${opt.out}`);
