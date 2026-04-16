# semtx - Tasks List

## Phase 1: Core CSS Foundation

1. [x] Create CSS custom properties for colors (Latte light + Mocha dark), typography, spacing scale, borders, shadows
2. [x] Implement minimal CSS reset (box-sizing, margins, typography base)
3. [x] Build utility classes (display, flex, grid, spacing, sizing, responsive prefixes)
4. [x] Create button components with all variants (primary, secondary, outline, ghost, danger, link) and sizes (sm, md, lg)
5. [x] Build form input styles (input, textarea, select, checkbox, radio, file, switch) with states

## Phase 2: Components

6. [x] Create card component (header, body, footer) with variants (default, flat, outline)
7. [x] Build navigation components (navbar, sidebar, tabs, breadcrumb, pagination)
8. [x] Create alert styles (info, success, warning, error) with dismissible feature using data-close
9. [x] Build table styles (striped, hoverable, responsive wrapper, bordered)
10. [x] Create modal styles (CSS-driven with data attributes, backdrop, header, body, footer, sizes)
11. [x] Add skeleton (text, wave animation) and toast (auto-dismiss) components

## Phase 3: HTMX Integration

12. [x] Add HTMX loading state classes (.htmx-indicator, .htmx-request, .htmx-requesting)
13. [x] Implement swap transitions (.htmx-swapping, .htmx-settling with opacity fades)
14. [x] Add active/navigate state styles (.htmx-history-navigate)

## Phase 4: Demo Page

15. [x] Build index.html showcasing all components with live examples (buttons, forms, cards, nav, alerts, tables, modals, skeletons)
16. [x] Add theme toggle (light/dark switch) and verify responsiveness across breakpoints

## Phase 5: Polish

17. [x] Verify reduced motion support and accessibility (focus states, contrast, touch targets)
18. [x] Final code review, minify CSS, update README with usage documentation

## Phase 6: HTMX Patterns (New)

### 6.1 Enhanced Loading Indicators
19. [x] Polished spinner animation (CSS-only with keyframes)
20. [x] Progress bar component with determinate/indeterminate states
21. [x] Slim progress bar for inline loading

### 6.2 Active Search
22. [x] Search input with integrated indicator (.input-search)
23. [x] Search results container with loading state

### 6.3 Click to Load / Pagination
24. [x] Load more button (.btn-load-more) with built-in loading state
25. [x] Pagination component with HTMX indicators

### 6.4 Infinite Scroll
26. [x] Infinite scroll trigger styles (.infinite-scroll-trigger)
27. [x] Scroll-sentinel element

### 6.5 Linked Selects
28. [x] Select with loading indicator (.select-loading)

### 6.6 Lazy Load
29. [x] Lazy load placeholder styles
30. [x] Fade-in animation for lazy content

### 6.7 JS Helpers
31. [x] Debounced search helper function (inline in demo)
32. [x] Progress bar simulation (inline in demo)
33. [x] Extended modal/Loading helpers

### 6.8 Demo Updates
34. [x] Add HTMX Patterns demos to index.html
35. [x] Test all patterns with live examples