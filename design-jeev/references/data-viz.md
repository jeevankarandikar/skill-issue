# Charts and data

Load this for dashboards, analytics and any screen with a chart. Start from the relationship in the data and the one sentence the chart should leave behind. That sentence decides the chart type, its title and where the emphasis color goes.

## Pick the chart from the relationship

The grouping follows the Financial Times Visual Vocabulary and Datawrapper's guidance.

| Relationship | First choice | Also works | Avoid when |
| --- | --- | --- | --- |
| Change over time | Line | Area, columns for few points, slope | Fewer than 4 points, or more than 6 series |
| Magnitude | Bar or column | Lollipop, dot plot | |
| Ranking | Ordered bar | Dot strip, slope | |
| Part to whole | Stacked bar | Pie or donut, treemap, waffle | Pie with more than 5 slices or small differences |
| Deviation from a baseline | Diverging bar | Diverging stacked bar | |
| Distribution | Histogram, box plot | Violin, beeswarm | Fewer than 20 points per group |
| Correlation | Scatter | Bubble for a third variable, heatmap | Categorical variables, which want grouped bars |
| Flow | Sankey | Alluvial, chord, waterfall | |
| Spatial | Choropleth | Symbol map | Regions of very different size, which want a bar |

- On a small screen, prefer horizontal bars to columns so the labels stay readable.
- Past about seven colors, change the chart type.
- A pie gives a rough impression. Bars show a 3% difference that a pie cannot.
- Under about 1,000 points, draw vectors. Up to about 10,000, draw to a canvas and downsample. Beyond that, aggregate first.

## Palettes that survive color blindness

Lightness does the work for color-blind readers, so never place two hues of the same lightness side by side.

Categorical, for unordered groups:

- Okabe-Ito: `#E69F00 #56B4E9 #009E73 #F0E442 #0072B2 #D55E00 #CC79A7 #000000`
- Tableau Color Blind 10: `#006BA4 #FF800E #ABABAB #595959 #5F9ED1 #C85200 #898989 #A2C8EC #FFBC79 #CFCFCF`
- ColorBrewer Dark2: `#1B9E77 #D95F02 #7570B3 #E7298A #66A61E #E6AB02 #A6761D #666666`

Sequential, for low to high:

- Blues: `#EFF3FF #BDD7E7 #6BAED6 #3182BD #08519C`
- YlGnBu: `#FFFFCC #A1DAB4 #41B6C4 #2C7FB8 #253494`

Diverging, around a midpoint in light grey:

- RdBu: `#CA0020 #F4A582 #F7F7F7 #92C5DE #0571B0`
- BrBG: `#A6611A #DFC27D #F5F5F5 #80CDC1 #018571`

Avoid red to green scales such as RdYlGn and Spectral. Check any hex value against colorbrewer2.org before shipping it. A project's own chart tokens in `DESIGN.md` come first, and these palettes fill in where it has none.

## Access

- Tell series apart by shape, pattern or a direct label as well as color.
- Bars with visible value labels are the most accessible chart. Lines need different line styles per series.
- A pie or donut ships with a data table beside it.
- Network graphs and 3D charts are never the primary chart in a product.
- Every chart has a text summary of its takeaway that a screen reader can reach. Native chart frameworks often provide per-interval descriptions; use them.
