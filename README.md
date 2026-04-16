# semtx

A minimal, modern CSS framework designed for HTMX-powered applications. Built with semantic HTML and CSS-3, semtx provides seamless loading states, swap transitions, and native HTMX class support without any JavaScript dependencies.

## Features

- **HTMX-Native**: First-class support for HTMX loading states, indicators, and swap transitions
- **Semantic HTML**: Class names reflect purpose, not style (e.g., `.card-body`, `.btn-primary`)
- **Zero Dependencies**: Single CSS file, no JavaScript required
- **Dark Mode**: Automatic dark mode detection with manual override support
- **Accessible**: Focus states, reduced motion support, 44px minimum touch targets
- **Modern CSS**: Uses CSS custom properties, color-mix, and modern layout techniques

## Quick Start

```html
<link rel="stylesheet" href="semtx.css">
<script src="https://unpkg.com/htmx.org"></script>
```

## Theming

semtx uses CSS custom properties. Override them in your CSS:

```css
:root {
  --primary: #your-color;
  --bg-base: #your-bg;
}
```

### Dark Mode

```html
<!-- Auto-detected via prefers-color-scheme -->
<html class="dark"> <!-- Manual dark mode -->
```

## Components

### Buttons

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-outline">Outline</button>
<button class="btn btn-ghost">Ghost</button>
<button class="btn btn-danger">Danger</button>
```

Sizes: `.btn-sm`, `.btn-lg`

### Forms

```html
<div class="form-group">
  <label class="form-label">Email</label>
  <input type="email" class="form-input" placeholder="you@example.com">
</div>

<textarea class="form-input textarea"></textarea>
<select class="form-input select">...</select>

<label class="switch">
  <input type="checkbox">
  <span class="switch-track"></span>
</label>
```

### Cards

```html
<div class="card">
  <div class="card-header">Title</div>
  <div class="card-body">Content</div>
  <div class="card-footer">Actions</div>
</div>
```

### Navigation

```html
<!-- Navbar -->
<nav class="navbar">
  <a class="navbar-brand" href="/">Brand</a>
  <ul class="navbar-nav">
    <li><a href="#">Link</a></li>
  </ul>
</nav>

<!-- Tabs -->
<div class="tabs">
  <button class="tab active">Tab 1</button>
  <button class="tab">Tab 2</button>
</div>

<!-- Breadcrumb -->
<ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="/">Home</a></li>
  <li class="breadcrumb-item"><a href="/products">Products</a></li>
  <li class="breadcrumb-item active"><span>Item</span></li>
</ol>

<!-- Pagination -->
<ul class="pagination">
  <li><a href="?page=1">1</a></li>
  <li><a href="?page=2">2</a></li>
</ul>
```

### Alerts

```html
<div class="alert alert-info">
  <span class="alert-icon">ℹ️</span>
  <div class="alert-content">
    <div class="alert-title">Info</div>
    Message here
  </div>
</div>

<div class="alert alert-success">...</div>
<div class="alert alert-warning">...</div>
<div class="alert alert-error">...</div>
```

### Modals

```html
<div class="modal" id="my-modal">
  <div class="modal-backdrop" data-modal-close></div>
  <div class="modal-content">
    <div class="modal-header">
      Title
      <button class="modal-close" data-modal-close>×</button>
    </div>
    <div class="modal-body">Content</div>
    <div class="modal-footer">
      <button class="btn btn-secondary" data-modal-close>Cancel</button>
      <button class="btn btn-primary">Confirm</button>
    </div>
  </div>
</div>
```

Sizes: `.modal-sm`, `.modal-lg`, `.modal-full`

### Tables

```html
<div class="table-wrapper">
  <table class="table table-striped table-hover">
    <thead>
      <tr><th>Name</th><th>Email</th></tr>
    </thead>
    <tbody>
      <tr><td>John</td><td>john@example.com</td></tr>
    </tbody>
  </table>
</div>
```

### Badges

```html
<span class="badge badge-primary">New</span>
<span class="badge badge-success">Active</span>
<span class="badge badge-warning">Pending</span>
<span class="badge badge-error">Error</span>
<span class="badge badge-dot"></span>
```

### Skeleton Loaders

```html
<div class="skeleton skeleton-text"></div>
<div class="skeleton skeleton-circle skeleton-avatar"></div>
<div class="skeleton skeleton-line"></div>
```

## HTMX Integration

### Loading Indicator

```html
<button class="btn btn-primary" hx-get="/data" hx-indicator=".loading">
  Load Data
  <span class="htmx-indicator loading">Loading...</span>
</button>
```

### Progress Bar

```html
<div class="progress">
  <div class="progress-bar" style="width: 75%"></div>
</div>

<!-- Indeterminate -->
<div class="progress">
  <div class="progress-bar indeterminate"></div>
</div>
```

### Search with Loading

```html
<div class="input-search">
  <input type="search" class="form-input" hx-get="/search" hx-trigger="keyup changed delay:300ms">
  <span class="input-search-icon">🔍</span>
  <span class="htmx-indicator spinner"></span>
</div>
```

### Infinite Scroll

```html
<div class="infinite-scroll-trigger" hx-get="/more" hx-trigger="revealed">
  <span class="htmx-indicator">Loading more...</span>
</div>
```

### Load More Button

```html
<button class="btn btn-secondary btn-load-more" hx-get="/more">
  Load More
</button>
```

### Inline Edit

```html
<div class="inline-edit" data-editable>
  <div class="inline-edit-view">
    Click to edit
  </div>
  <form class="inline-edit-form">
    <input type="text" class="form-input" value="Click to edit">
  </form>
</div>
```

## Utility Classes

### Layout

```html
<div class="container">
  <div class="flex gap-4">
    <div class="flex-1">Main</div>
    <div class="sidebar-layout">Sidebar</div>
  </div>
</div>
```

Classes: `.flex`, `.flex-col`, `.grid`, `.between`, `.centered`, `.stack`

### Spacing

```html
<div class="p-4 m-4 mt-2 mb-2 gap-2">...</div>
```

### Typography

```html
<h1 class="title-lg">Title</h1>
<p class="lead">Lead text</p>
<span class="text-muted">Muted</span>
```

### Responsive

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
  ...
</div>
```

## Design Tokens

| Token | Description |
|-------|-------------|
| `--primary` | Main brand color |
| `--text`, `--text-sub` | Text colors |
| `--bg-base`, `--bg-surface`, `--bg-mantle` | Background layers |
| `--border` | Border color |
| `--red`, `--peach`, `--yellow`, `--green`, `--teal`, `--sky`, `--blue` | Accent colors |
| `--radius` | Border radius |
| `--shadow` | Box shadow |
| `--trans` | Transition timing |

## Accessibility

- Focus visible outlines (2px)
- Reduced motion support via `prefers-reduced-motion`
- Minimum 44x44px touch targets
- Semantic HTML structure

## Browser Support

Modern browsers (last 2 versions): Chrome, Firefox, Safari, Edge

## License

MIT
