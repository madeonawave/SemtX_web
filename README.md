# semtx

A Django-powered demo and showcase for semtx, a minimal CSS framework designed for HTMX-powered applications.

## What is semtx?

semtx is a lightweight, modern CSS framework built specifically for HTMX applications. It provides:

- **HTMX-Native**: First-class support for loading states, indicators, and swap transitions
- **Catppuccin Colors**: Beautiful light and dark themes
- **Zero Dependencies**: Single CSS file, no JavaScript required for styling
- **Accessible**: Focus states, reduced motion support, 44px minimum touch targets

## Project Structure

```
semtx_new/
├── src/
│   ├── config/          # Django settings
│   └── main/            # Main app
│       ├── static/      # CSS, JS, images
│       └── templates/   # HTML templates
├── pyproject.toml
└── manage.py
```

## Demo Features

The demo showcases:

- **Components**: Buttons, forms, cards, tables, modals, alerts
- **Navigation**: Navbar, tabs, breadcrumbs, pagination
- **HTMX Patterns**: Loading indicators, progress bars, infinite scroll, search with debounce
- **Theming**: Light/dark mode with Catppuccin colors
- **Utilities**: Layout, spacing, typography classes

## CSS Framework

The CSS file is located at `src/main/static/css/semtx.css`. Key features:

- CSS custom properties for theming
- Semantic class names (e.g., `.card-body`, `.btn-primary`)
- Responsive breakpoints (sm: 640px, md: 768px, lg: 1024px)
- HTMX-specific classes (`.htmx-indicator`, `.htmx-request`)

