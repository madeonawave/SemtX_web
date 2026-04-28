"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from main.views import (
    demo_view,
    search_view,
    load_more_view,
    infinite_scroll_view,
    load_options_view,
    tab_content_view,
    breadcrumb_content_view,
    pagination_content_view,
    modal_content_view,
    pending_content_view,
    philosophy_view,
    dialog_content_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", demo_view, name="demo"),
    path("philosophy", philosophy_view, name="philosophy"),
    path("search", search_view, name="search"),
    path("load-more", load_more_view, name="load_more"),
    path("infinite-scroll", infinite_scroll_view, name="infinite_scroll"),
    path("load-options", load_options_view, name="load_options"),
    path("tab-content", tab_content_view, name="tab_content"),
    path("breadcrumb-content", breadcrumb_content_view, name="breadcrumb_content"),
    path("pagination-content", pagination_content_view, name="pagination_content"),
    path("modal-content", modal_content_view, name="modal_content"),
    path("dialog-content", dialog_content_view, name="dialog_content"),
    path("pending-content", pending_content_view, name="pending_content"),
]
