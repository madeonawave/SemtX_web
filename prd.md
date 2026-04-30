# semtx - Product Requirements Document

## 1. Project Overview

**Project Name:** semtx  
**Type:** CSS-only framework  
**Core Functionality:** A minimal, modern CSS framework designed for HTMX-powered applications with seamless loading states, swap transitions, and native HTMX class support.  
**Target Users:** Web developers building HTMX-based web applications who want a lightweight, production-ready CSS solution.

---

## 2. Design System

### 2.1 Color Palette (Catppuccin)

**Light Theme (Latte):**
| Role | Color | OKLCH | Hex |
|------|-------|-------|-----|
| Primary | Mauve | oklch(55% 25% 297deg) | #8839ef |
| Text | Text | oklch(44% 4% 279deg) | #4c4f69 |
| Subtext | Subtext 1 | oklch(49% 4% 279deg) | #5c5f77 |
| Surface | Surface 0 | oklch(86% 1% 268deg) | #ccd0da |
| Base | Base | oklch(96% 1% 265deg) | #eff1f5 |
| Mantle | Mantle | oklch(93% 1% 265deg) | #e6e9ef |

**Dark Theme (Mocha):**
| Role | Color | OKLCH | Hex |
|------|-------|-------|-----|
| Primary | Mauve | oklch(79% 12% 305deg) | #cba6f7 |
| Text | Text | oklch(88% 4% 272deg) | #cdd6f4 |
| Subtext | Subtext 1 | oklch(82% 4% 273deg) | #bac2de |
| Surface | Surface 0 | oklch(32% 3% 282deg) | #313244 |
| Base | Base | oklch(24% 3% 284deg) | #1e1e2e |
| Mantle | Mantle | oklch(22% 3% 284deg) | #181825 |

**Accent Colors:**
| Role | Light Hex | Dark Hex |
|------|----------|----------|
| Red | #d20f39 | #f38ba8 |
| Peach | #fe640b | #fab387 |
| Yellow | #df8e1d | #f9e2af |
| Green | #40a02b | #a6e3a1 |
| Blue | #1e66f5 | #89b4fa |
| Sky | #04a5e5 | #89dceb |
| Teal | #179299 | #94e2d5 |

### 2.2 Typography

- **Font Family:** System font stack: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
- **Monospace:** `"IBM Plex Mono", "Fira Code", Consolas, monospace`
- **Base Size:** 16px (1rem)
- **Scale:** 1.25 (Minor Third)
  - xs: 0.75rem | sm: 0.875rem | base: 1rem | lg: 1.125rem | xl: 1.25rem | 2xl: 1.563rem | 3xl: 1.953rem | 4xl: 2.441rem

### 2.3 Spacing & Layout

- **Scale (rem):** 0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 6, 8, 12, 16
- **Breakpoints:** sm: 640px | md: 768px | lg: 1024px | xl: 1280px

### 2.4 Borders & Radius

- **Radius:** none: 0 | sm: 0.25rem | DEFAULT: 0.5rem | lg: 0.75rem | FULL: 9999px
- **Border Width:** 1px default, 2px focus

### 2.5 Transitions

- **Duration:** 150ms, 200ms, 300ms
- **Timing:** ease, ease-in, ease-out
- **Default:** 200ms ease

---

## 3. HTMX Integration

### 3.1 Loading States
```css
.htmx-request { opacity: 0.6; pointer-events: none; }
.htmx-indicator { display: none; }
.htmx-indicator.htmx-requesting { display: inline; spin animation; }
```

### 3.2 Swap Transitions
```css
.htmx-swapping { opacity: 0; transition: opacity 200ms ease-out; }
.htmx-settling { opacity: 1; transition: opacity 200ms ease-in; }
```

### 3.3 Active States
- `.htmx-history-navigate` for back/forward navigation

---

## 4. Components

### 4.1 Buttons
- Variants: `.btn-primary`, `.btn-secondary`, `.btn-outline`, `.btn-ghost`, `.btn-danger`, `.btn-link`
- Sizes: `.btn-sm`, `.btn-md`, `.btn-lg`
- States: `:disabled`, `.loading`

### 4.2 Form Inputs
- Elements: `.input`, `.textarea`, `.select`, `.checkbox`, `.radio`, `.file`, `.switch`
- States: `:disabled`, `:invalid`, `:valid`, `:focus`

### 4.3 Cards
- Structure: `.card-header`, `.card-body`, `.card-footer`
- Variants: default, flat, outline

### 4.4 Navigation
- Components: `.navbar`, `.sidebar`, `.tabs`, `.breadcrumb`, `.pagination`

### 4.5 Alerts
- Variants: `.alert-info`, `.alert-success`, `.alert-warning`, `.alert-error`
- Feature: `.alert-dismissible` with `data-close`

### 4.6 Modals (CSS-driven)
- Trigger: `data-modal="#modal-id"`
- Close: `data-modal-close`, backdrop click
- Sizes: `.modal-sm`, `.modal-md`, `.modal-lg`, `.modal-full`

### 4.7 Tables
- Features: `.table-striped`, `.table-hover`, `.table-responsive`, `.table-bordered`

### 4.8 Badges
- Variants: `.badge`, `.badge-dot`

### 4.9 Additional
- Toasts: `.toast`, `.toast-container`
- Skeleton: `.skeleton`, `.skeleton-text`, `.skeleton-wave`
- Typography: `.prose` wrapper

---

## 5. Utility Classes

- **Layout:** `.container`, `.grid`, `.flex`, `.flex-col`, `.inline-flex`
- **Display:** `.block`, `.inline`, `.inline-block`, `.hidden`
- **Spacing:** `.m{N}`, `.mt{N}`, `.mb{N}`, `.ml{N}`, `.mr{N}`, `.mx{N}`, `.my{N}`, `.p{N}`, `.pt{N}`, `.pb{N}`, `.pl{N}`, `.pr{N}`, `.px{N}`, `.py{N}`
- **Sizing:** `.w-full`, `.h-full`, `.max-w-{...}`
- **Responsive:** `sm:`, `md:`, `lg:`, `xl:` prefixes

---

## 6. Theme Support

- CSS custom properties with `:root` (light) and `:root.dark` (dark)
- Auto-detect via `prefers-color-scheme` media query

---

## 7. Accessibility

- Focus visible: 2px outline
- Reduced motion: `@media (prefers-reduced-motion)`


---

## 8. File Structure

```
semtx/
├── semtx.css    # Single file, all components
├── index.html   # Demo page with all examples
└── README.md   # Documentation
```

---

## 9. Browser Support

- Modern browsers (last 2 versions): Chrome, Firefox, Safari, Edge
- No IE11 support

---

## 10. Success Criteria

1. Single CSS file under 30KB minified
2. All components responsive (mobile-first)
3. Theme switchable via CSS custom properties
4. HTMX classes work without JS
5. No external dependencies
6. Lighthouse accessibility score 95+