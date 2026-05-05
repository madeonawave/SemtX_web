# semtx

This is the website for https://semtx.org 

A Django-powered demo and showcase for Semtx CSS, a minimal CSS library.

## What is Semtx?

Semtx is a lightweight, modern, (mostly) Semantic CSS library. 

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
- Semantic class names (e.g., `article`, `button`, `.btn-primary`)
- Responsive breakpoints
- HTMX-specific classes for transitions, loaders/ spinner

