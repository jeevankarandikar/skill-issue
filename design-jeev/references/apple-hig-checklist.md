# Apple HIG review checklist

Pass or fail review for any Apple-platform interface or Apple-style web UI. Each line names the HIG page behind it; the details are on that page at developer.apple.com/design/human-interface-guidelines.

How to run it: open the surface at a narrow window and a wide one, in light and dark, with the keyboard only and then with the pointer. Mark each line pass, fail, or not applicable, and give a location for every fail. Untested counts as fail. Where a line collides with a numbered open item in the project's `DESIGN.md`, report the open item by number instead of a fail.

## Hierarchy and layout
- [ ] The most important content sits at the top and leading side, and reading order matches visual order in the DOM. (Layout)
- [ ] Each screen has one clear purpose and one `<h1>`; section headings form a real outline. (Layout, VoiceOver)
- [ ] Related items are grouped by space or one level of container, with no nested boxes. (Layout, Boxes)
- [ ] Controls sit next to what they change; nothing critical sits at the bottom of a Mac window or sidebar. (Layout, Sidebars)
- [ ] At the narrowest and widest window sizes nothing clips, overlaps or scrolls sideways, and features stay the same with only visibility changing. (Layout)
- [ ] A Mac layout uses a sidebar with detail at desktop widths, with no iOS bottom tab bar. (Sidebars, Tab bars, Mac Catalyst)

## One primary action
- [ ] Each view has at most one prominent, accent-filled action, placed last in its group. (Buttons, Toolbars)
- [ ] Preference is shown by style, and all buttons in a set share one size. (Buttons)
- [ ] The accent color marks only the primary action, selection and status. (Branding, Color)
- [ ] A destructive action is never the default button and never the Return target. (Buttons, Alerts)

## Spacing and targets
- [ ] Mac controls are at least 28 by 28 pt (20 pt floor); touch surfaces at least 44 by 44 pt. (Accessibility, Buttons)
- [ ] Hit areas extend about 12 pt past bezeled controls and 24 pt past borderless icon buttons, with no dead gaps between toolbar buttons. (Pointing devices)
- [ ] Spacing uses a consistent scale, and hover and focus effects are never cropped by neighbors. (Collections, Layout)

## Type scale
- [ ] Interface text asks the system first (`-apple-system, system-ui`), with a self-hosted open face after it only where the system is not enough. (Typography, owner decision 2026-09-15)
- [ ] Mac UI body text is 13px with nothing below 10px; other sizes come from the platform style table. (Typography)
- [ ] Weights stay between 400 and 700 with no ultralight, thin or light text. (Typography)
- [ ] Sizes are in rem, and the page stays usable at 200 percent zoom, wrapping rather than truncating in scrolling content. (Accessibility, Typography)
- [ ] No manual letter-spacing on system text. (Typography)

## Contrast and color
- [ ] Body text reaches 4.5:1 and large or bold text 3:1, measured in both light and dark. (Accessibility, Color)
- [ ] No state, status or chart series is shown by color alone. (Accessibility, Color, Charts)
- [ ] Colors come from semantic tokens by role; no separator color on text and no hard-coded system RGB values. (Color)
- [ ] `prefers-contrast: more` raises contrast. (Color, Dark Mode)

## Dark mode
- [ ] First paint follows `prefers-color-scheme` with no white flash, and `color-scheme: light dark` is set. (Dark Mode, Launching)
- [ ] The dark palette uses dimmer grounds and brighter text rather than an inversion, and white-background images are dimmed. (Dark Mode)
- [ ] Icons use `currentColor` or have per-mode variants, and still read in both modes. (Dark Mode, Icons)
- [ ] The product follows the system appearance with no toggle and no stored override. A published artifact instead opens on its default palette and has a working theme switch. (Dark Mode, owner artifact rule)

## Focus and keyboard
- [ ] Every control can be reached with Tab in reading order, with no positive tabindex. (Keyboards, Focus and selection)
- [ ] A visible `:focus-visible` ring shows on every focusable element; `outline: none` never appears without a replacement. (Focus and selection)
- [ ] Lists and grids are one tab stop with arrow keys inside, and selection turns gray when the window or list loses focus. (Focus and selection)
- [ ] Focus never moves on its own after load or async updates, and dialogs return focus to their opener. (Focus and selection, Modality)
- [ ] Escape closes overlays, Command-Period cancels running work, and page script never swallows Command-C, V, Z, F, W, Q or Comma. (Keyboards)
- [ ] Every command also exists as a menu bar item in the Mac shell, or in a visible home plus a command palette in the browser build. (The menu bar, Toolbars)
- [ ] Each shortcut is shown with glyphs in Control, Option, Shift, Command order. (Keyboards)
- [ ] Buttons use `cursor: default` and only links use the pointing hand. (Pointing devices)

## Motion and system settings
- [ ] Nonessential animation only runs under `prefers-reduced-motion: no-preference`; under reduce, changes are instant or short fades with no blur animation. (Motion, Accessibility)
- [ ] Each accessibility setting the page can read has a tested branch: `prefers-reduced-motion`, `prefers-reduced-transparency` (solid surfaces instead of blur), `prefers-contrast: more` and `forced-colors: active`. (Accessibility, Materials)
- [ ] Motion never carries information alone, never blocks input, and can be interrupted from where it is. (Motion)
- [ ] Hover, selection, tab switches and typing have no motion. (Motion)
- [ ] Scrolling stays native, with no scroll-jacking and no script that changes scroll speed or snaps the page. (Scroll views, Motion)
- [ ] Nothing autoplays with sound, and any looping video has a pause control. (Accessibility, Playing video)

## Permission timing and privacy
- [ ] No permission request appears at launch; each one appears when the feature that needs it is first used. (Privacy, Onboarding)
- [ ] Any pre-permission screen has one button that leads to the system request, labeled like Continue and never Allow, with no bypass. (Privacy)
- [ ] Visible text says what is read, where it stays, and exactly when anything leaves the device. (Privacy, Generative AI)
- [ ] Secrets go in the keychain and password-type fields, never prefilled or echoed. (Privacy, Entering data)

## Assets and licenses
- [ ] No file from Apple's Design Resources downloads appears anywhere: no SF Pro, New York or SF Mono file, no SF Symbols export or symbol font, no UI kit asset or exported token, no bezel, no badge. (owner decision 2026-09-15)
- [ ] Web icons are Lucide inline SVG, with Phosphor regular for a missing glyph, stroked with `currentColor` at a weight matched to the adjacent text. SF Symbols appear only in native Swift code. (Icons, SF Symbols)
- [ ] Every bundled font and icon set has its license file beside it and a line in the third-party notices file. (owner decision 2026-09-15)
- [ ] Screenshots use fictional data only and sit in the project's own frame, with no traffic-light dots and no Apple device shape. (App Store marketing guidelines)
- [ ] Mac and other Apple product names are written as Apple writes them, and no Apple logo appears. (App Store marketing guidelines)

## Progressive disclosure
- [ ] Common controls are visible and advanced options start hidden behind a labeled disclosure. (Disclosure controls)
- [ ] A sidebar or menu goes no deeper than two levels, and a submenu no deeper than one. (Sidebars, Menus)
- [ ] Onboarding does real work, every step can be skipped, a skipped tour stays skipped, and setup is deferred behind good defaults. (Onboarding)
- [ ] Nothing essential appears only on hover. (Offering help)

## Button, menu and label copy
- [ ] Labels are short verbs that name the result, with no "OK" where a specific verb fits and no Yes or No. (Writing, Alerts)
- [ ] Link text names the destination, never "click here". (Writing)
- [ ] Commands that need more input end in the single ellipsis character. (Menus, Buttons)
- [ ] Capitalization follows Apple per element: title style for menus, buttons, tabs, column headings and segments, sentence style for alerts, box titles, slider labels and tooltips. The Mac verb is click, and Apple product names keep their capitals. (Writing, Menus, Alerts)
- [ ] Icon-only buttons have an accessible name and a tooltip describing the action. (Buttons, Offering help)
- [ ] Every field has a visible label, and placeholders show format only. (Text fields, Entering data)

## Alerts and feedback
- [ ] Alerts are used only for rare, critical, actionable events, never to inform, never at launch, and never for undoable actions. (Alerts, Feedback)
- [ ] An alert title says what happened and why; buttons put Cancel on the leading side and the default on the trailing side, and there is only one dialog at a time. (Alerts, Modality)
- [ ] Destructive actions that cannot be undone are confirmed; common destructive actions offer undo instead. (Alerts, Undo and redo)
- [ ] Errors appear next to the problem with a fix, no blame, and `aria-invalid` plus a described message. (Writing, Entering data)
- [ ] Status appears near its subject and is announced through `role="status"` or a polite live region. (Feedback, VoiceOver)

## Loading and empty states
- [ ] Something real renders immediately (a shell or skeleton), and the UI stays usable while data loads. (Loading)
- [ ] Progress is determinate whenever the duration is known, moves at an honest pace, names the task, and offers Cancel. (Progress indicators, Generative AI)
- [ ] Spinners wait briefly before showing so fast loads never flash them. (Loading)
- [ ] Every empty state explains why it is empty and offers a button that does the next step, with no crucial information hidden there. (Writing, Tab bars)
- [ ] Missing data is stated in words, never shown as a blank or a zero. (Workouts, Charts)
- [ ] Relaunch restores the last view, scroll position and window frame. (Launching, Multitasking)

## Reporting

List findings most severe first, and give each one a location, the HIG page and the change to make.

- P0 blocks shipping: a task that cannot be finished, a control a keyboard or VoiceOver user cannot reach, a privacy leak, or an Apple-licensed asset in the build.
- P1 gets fixed before the next release: a departure people will notice, such as a missing focus ring, a permission prompt at launch, two competing primary actions or text under 4.5:1.
- P2 is polish in spacing, alignment, copy and motion.
- Open items come after P2, by number, each with the surfaces it touches.
