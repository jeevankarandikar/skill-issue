# Data Visualization

Chart selection + accessible palettes for dashboards and analytics. Lead with the data *relationship*, then pick the chart — not the other way around.

## Pick the chart from the relationship

Taxonomy from the FT Visual Vocabulary, cross-checked with Datawrapper.

| Relationship | Primary | Secondary | Avoid / not when |
|---|---|---|---|
| **Change over time** | Line | Area, column (few points), slope | <4 points; >6 series |
| **Magnitude** (compare sizes) | Bar / Column | Lollipop, dot plot | — |
| **Ranking** | Ordered bar | Dot strip, slope | — |
| **Part-to-whole** | Stacked bar | Pie/donut, treemap, waffle | Pie when >5 slices or diffs <5% (fails precise reads + colorblind) |
| **Deviation** (± vs baseline) | Diverging bar | Diverging stacked bar | — |
| **Distribution** | Histogram, Box plot | Violin, beeswarm | <20 points per group |
| **Correlation** | Scatter | Bubble (3rd var), heatmap | categorical vars → grouped bar |
| **Flow** | Sankey | Alluvial, chord, waterfall | — |
| **Spatial** | Choropleth | Symbol map, cartogram | regions of very different size → use a bar |

**Cross-cutting heuristics:**
- **Small screens: bar over column** — bars grow vertically and keep labels readable; columns overflow horizontally.
- **Cap at ~7 colors.** "If you need more than seven colors, use another chart type" (Datawrapper).
- **Pie is for rough impressions only.** Bar/column read 3% differences a pie can't.
- **The chart's one-sentence takeaway** drives its type, title, and color emphasis.
- **Volume → renderer:** <1k points SVG · 1k–10k Canvas + downsample · >10k aggregate · 3D/large-geo → WebGL.

## Accessible palettes (colorblind-safe, verified hex)

Lightness variation is what saves colorblind readers — don't place two same-lightness hues side by side.

**Categorical** (distinct unordered categories; vary hue, ≤7):
- **Okabe-Ito** (8, gold standard): `#E69F00 #56B4E9 #009E73 #F0E442 #0072B2 #D55E00 #CC79A7 #000000`
- **Tableau Color Blind 10**: `#006BA4 #FF800E #ABABAB #595959 #5F9ED1 #C85200 #898989 #A3C8EC #FFBC79 #CFCFCF`
- **ColorBrewer Dark2** (CVD- + print-safe): `#1B9E77 #D95F02 #7570B3 #E7298A #66A61E #E6AB02 #A6761D #666666`

**Sequential** (ordered low→high; encode by lightness):
- **Blues**: `#EFF3FF #BFD3E6 #6BAED6 #3182BD #08519C`
- **YlGnBu** (multi-hue, better discrimination): `#FFFFCC #A1DAA6 #41B6C4 #2C7FB8 #253494`

**Diverging** (deviation from a midpoint; center light grey, not white):
- **RdBu** (CVD-safe): `#CA0020 #F4A582 #F7F7F7 #92C5DE #0571B0`
- **BrBG** (preferred over red-green): `#A6611A #DFC27D #F5F5F5 #80CED7 #018571`
- **Avoid** `RdYlGn`, `Spectral` — red-green confusion.

## Accessibility (grade every chart)

Adopt a grade + mandatory-fallback model:
- **AAA**: bar, bullet (value labels always visible).
- **AA**: line — differentiate series by line *style*, not color alone.
- **C**: pie/donut — must ship a stacked-bar alternative + a data-table fallback.
- **D**: network graph, 3D scatter/surface — never a primary chart in product UI.
- Differentiate series by **shape / pattern / direct labels, not color alone.**
- **Apple/Swift Charts** gives VoiceOver labels + audio graphs automatically — create an accessibility element *per interval*, not per data point.

---

**Avoid**: pie for precise comparison · >7 colors · `RdYlGn`/Spectral (colorblind-unsafe) · color as the only differentiator · 3D/network charts as primary UI. Sources: FT Visual Vocabulary (`Financial-Times/chart-doctor`), Datawrapper Academy, ColorBrewer, Okabe-Ito (Nature Methods), Apple HIG charting.
