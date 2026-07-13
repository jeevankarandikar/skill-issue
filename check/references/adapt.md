# `/check adapt` — patterns and snippets

### Mobile Adaptation (Desktop → Mobile)

**Layout**: Single column. Vertical stacking. Full-width components. Max-width: 100%.

**Interaction**: Touch targets 44x44px minimum. Swipe gestures for lists/carousels. Bottom sheets instead of dropdowns. Thumbs-first design (controls in thumb reach zone). Larger tap areas with more spacing.

**Content**: Progressive disclosure. Prioritize primary content. Shorter text. 16px minimum body text.

**Navigation**: Bottom navigation bar or hamburger drawer. Reduce navigation complexity. Sticky header for context. Back button in flow.

### Tablet Adaptation (Hybrid)

**Layout**: Two-column (not one or three). Side panels for secondary content. Master-detail views. Adaptive by orientation.

**Interaction**: Support both touch and pointer. 44x44px touch targets. Side navigation drawers. Multi-column forms where appropriate.

### Desktop Adaptation (Mobile → Desktop)

**Layout**: Multi-column (use horizontal space). Side navigation always visible. Multiple panels simultaneously. Fixed widths with max-width constraints (don't stretch to 4K).

**Interaction**: Hover states for additional information. Keyboard shortcuts. Right-click context menus. Drag-and-drop. Multi-select with Shift/Cmd.

**Content**: More information upfront (less progressive disclosure). Data tables with many columns. Richer visualizations.

### Print Adaptation

Page breaks at logical points. Remove navigation, footer, interactive elements. Black/white or limited color. Proper margins. Expand shortened content (full URLs, hidden sections). Add page numbers, headers, metadata. `@media print` stylesheet.

### Email Adaptation

600px max width. Single column only. Inline CSS (no external stylesheets). Table-based layouts for email client compatibility. Large, obvious CTAs (not text links). No hover states. Deep links to web app for complex interactions.

### Implementation Techniques

**Breakpoints** (content-driven, not arbitrary):
- Mobile: 320-767px
- Tablet: 768-1023px
- Desktop: 1024px+

**CSS**: Grid/Flexbox for automatic reflow. Container queries for container-based adaptation. `clamp()` for fluid sizing. Media queries for distinct context styles. `display: none` sparingly (still downloads).

**Touch**: 44x44px minimum tap targets. More spacing between interactive elements. Remove hover-dependent interactions. Add touch feedback (ripples, highlights).

**Responsive images**: `srcset`, `picture` element. Lazy loading for off-screen content.

**Navigation**: Hamburger/drawer on mobile. Bottom nav bar for apps. Persistent side nav on desktop. Breadcrumbs for context on small screens.

**Test on real devices**: DevTools emulation is helpful but not perfect. Test portrait and landscape. Safari, Chrome, Firefox, Edge. iOS, Android, Windows, macOS. Touch + mouse + keyboard. 320px (smallest), 4K (largest). Throttled network.
