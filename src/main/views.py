from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from time import sleep


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "semtx - CSS Framework for HTMX"
        return context


def demo_view(request):
    """Serve the demo page with semtx CSS framework"""
    return render(request, "index.html")


def philosophy_view(request):
    """Serve the philosophy page"""
    return render(request, "philosophy.html")


@csrf_exempt
def search_view(request):
    """HTMX endpoint for active search"""
    # Support both GET and POST
    if request.method == "GET":
        query = request.GET.get("q", "").lower()
    else:
        query = request.POST.get("q", "").lower()

    # Sample data
    all_users = [
        {"name": "Alice Johnson", "email": "alice@example.com"},
        {"name": "Bob Smith", "email": "bob@example.com"},
        {"name": "Carol White", "email": "carol@example.com"},
    ]

    # Filter - return all if no query (for initial load)
    if query:
        users = [
            u
            for u in all_users
            if query in u["name"].lower() or query in u["email"].lower()
        ]
    else:
        users = all_users

    # Return HTML - wrap in tbody for proper HTMX swapping
    html = "<tbody>"
    for user in users:
        html += f"<tr><td>{user['name']}</td><td>{user['email']}</td></tr>"
    html += "</tbody>"

    return HttpResponse(html)


@csrf_exempt
def load_more_view(request):
    """HTMX endpoint for load more button - follows htmx click-to-load pattern"""
    page = int(request.GET.get("page", 2))

    # All available items (page 1 shows first 2, page 2 shows next 2, etc.)
    all_items = [
        {"name": "Carol White", "email": "carol@example.com"},
        {"name": "David Brown", "email": "david@example.com"},
        {"name": "Eve Wilson", "email": "eve@example.com"},
        {"name": "Frank Miller", "email": "frank@example.com"},
        {"name": "Grace Lee", "email": "grace@example.com"},
        {"name": "Henry Clark", "email": "henry@example.com"},
        {"name": "Iris Johnson", "email": "iris@example.com"},
        {"name": "Jack Williams", "email": "jack@example.com"},
        {"name": "Kate Brown", "email": "kate@example.com"},
        {"name": "Liam Davis", "email": "liam@example.com"},
        {"name": "Mia Garcia", "email": "mia@example.com"},
        {"name": "Noah Martinez", "email": "noah@example.com"},
        {"name": "Olivia Rodriguez", "email": "olivia@example.com"},
        {"name": "Peter Wilson", "email": "peter@example.com"},
        {"name": "Quinn Anderson", "email": "quinn@example.com"},
        {"name": "Rachel Taylor", "email": "rachel@example.com"},
    ]

    # Items for this page (page 2 = items 3-4, page 3 = items 5-6, etc.)
    items_per_page = 2
    start = (page - 1) * items_per_page
    items = all_items[start : start + items_per_page]

    html = ""
    for item in items:
        html += '<div class="item p-2 border-b">'
        html += f'<div class="font-medium">{item["name"]}</div>'
        html += f'<div class="text-sm text-secondary">{item["email"]}</div>'
        html += "</div>"

    # If no more items, return empty to indicate end
    if start + items_per_page >= len(all_items):
        html = ""

    return HttpResponse(html)


@csrf_exempt
def infinite_scroll_view(request):
    """HTMX endpoint for infinite scroll - follows htmx infinite scroll pattern"""
    page = int(request.GET.get("page", 2))

    # All items for infinite scroll - starts from page 2 (index 0)
    all_items = [
        {"name": "Carol White", "email": "carol@example.com"},
        {"name": "David Brown", "email": "david@example.com"},
        {"name": "Eve Wilson", "email": "eve@example.com"},
        {"name": "Frank Miller", "email": "frank@example.com"},
        {"name": "Grace Lee", "email": "grace@example.com"},
        {"name": "Henry Clark", "email": "henry@example.com"},
        {"name": "Iris Johnson", "email": "iris@example.com"},
        {"name": "Jack Williams", "email": "jack@example.com"},
        {"name": "Kate Brown", "email": "kate@example.com"},
        {"name": "Liam Davis", "email": "liam@example.com"},
        {"name": "Mia Garcia", "email": "mia@example.com"},
        {"name": "Noah Martinez", "email": "noah@example.com"},
        {"name": "Olivia Rodriguez", "email": "olivia@example.com"},
        {"name": "Peter Wilson", "email": "peter@example.com"},
        {"name": "Quinn Anderson", "email": "quinn@example.com"},
        {"name": "Rachel Taylor", "email": "rachel@example.com"},
        {"name": "Sam Wilson", "email": "sam@example.com"},
        {"name": "Tina Martinez", "email": "tina@example.com"},
        {"name": "Uma Singh", "email": "uma@example.com"},
        {"name": "Victor Lee", "email": "victor@example.com"},
    ]

    items_per_page = 2
    start = (page - 2) * items_per_page  # page 2 starts at index 0
    items = all_items[start : start + items_per_page]

    # Return table rows only (item count updated client-side)
    html = ""
    for item in items:
        html += f"<tr><td>{item['name']}</td><td>{item['email']}</td></tr>"

    # Calculate remaining items
    remaining = len(all_items) - start - items_per_page

    # Include sentinel if there are more items
    if remaining > 0:
        next_page = page + 1
        html += f"""
        <tr hx-get="/infinite-scroll?page={next_page}"
            hx-swap="outerHTML"
            hx-target="this"
            hx-trigger="revealed once"
            data-loading-target="item-count">
          <td><span class="htmx-indicator"><span class="htmx-requesting.htmx-indicator"></span> Loading more...</span></td>
        </tr>
        """
    else:
        html += '<tr><td colspan="2" class="text-center text-secondary p-2">No more items</td></tr>'

    return HttpResponse(html)


@csrf_exempt
def load_options_view(request):
    """HTMX endpoint for loading select options"""
    options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

    html = '<select class="form-input select">'
    for opt in options:
        html += f'<option value="{opt.lower().replace(" ", "-")}">{opt}</option>'
    html += "</select>"

    return HttpResponse(html)


@csrf_exempt
def pending_content_view(request):
    """HTMX endpoint for pending/lazy load content"""
    html = "<p>Uses <code>.pending</code> with <code>.ready</code> for fade-in on load.</p><p>This content was loaded via HTMX and uses CSS transition for fades in...</p>"
    sleep(0.5)
    return HttpResponse(html)


@csrf_exempt
def tab_content_view(request):
    """HTMX endpoint for tab content"""
    tab = request.GET.get("tab", "dashboard")

    template_map = {
        "dashboard": "partials/tab_dashboard.html",
        "projects": "partials/tab_projects.html",
        "team": "partials/tab_team.html",
        "settings": "partials/tab_settings.html",
    }

    template_name = template_map.get(tab, None)

    if template_name:
        return render(request, template_name)
    else:
        return HttpResponse('<div class="p-4 text-secondary">Select a tab</div>')


@csrf_exempt
def breadcrumb_content_view(request):
    """HTMX endpoint for breadcrumb content"""
    import time

    time.sleep(0.5)

    page = request.GET.get("page", "")

    if page == "home":
        return render(request, "partials/breadcrumb_home.html")
    elif page == "products":
        return render(request, "partials/breadcrumb_products.html")
    elif page == "item":
        return render(request, "partials/breadcrumb_item.html")
    else:
        return HttpResponse(
            '<div class="p-4 text-center text-secondary">Select a page...</div>'
        )


@csrf_exempt
def pagination_content_view(request):
    """HTMX endpoint for pagination content"""
    import time

    time.sleep(0.3)

    page = request.GET.get("page", "1")

    if page == "1":
        return render(request, "partials/pagination_page1.html")
    elif page == "2":
        return render(request, "partials/pagination_page2.html")
    elif page == "3":
        return render(request, "partials/pagination_page3.html")
    else:
        return HttpResponse(
            '<div class="p-4 text-center text-secondary">Invalid page</div>'
        )


@csrf_exempt
def modal_content_view(request):
    """HTMX endpoint for modal content"""
    import time

    time.sleep(0.5)

    modal_type = request.GET.get("type", "default")

    if modal_type == "small":
        return render(request, "partials/modal_small.html")
    elif modal_type == "large":
        return render(request, "partials/modal_large.html")
    else:
        return render(request, "partials/modal_default.html")
