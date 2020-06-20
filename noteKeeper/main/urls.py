"""noteKeeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.shortcuts import render


app_name = 'main'

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('register/', views.register, name = 'register'),
    path('register/<single_slug>', views.error_page, name = 'error_page1'),
    path('login/', views.login_request, name = "login"),
    path('login/<single_slug>', views.error_page, name = 'error_page2'),
    path('logout/', views.logout_request, name = "logout"),
    path('notes/', views.department, name = "department"),
    path('notes/<single_slug>/', views.single_slug, name="single_slug"),
    path('notes/<slug:slug>/notes-list/', views.notes_list, name = "notes_list"),
    path('notes/<slug:slug>/notes-list/<int:pk>/', views.delete_notes, name = "delete_notes"),
    path('past-year-papers/', views.department, name = "papers_department"),
    path('past-year-papers/<single_slug>/', views.paper_single_slug, name="papers_single_slug"),
    path('past-year-papers/<slug:slug>/papers-list/', views.papers_list, name = "papers_list"),
    path('past-year-papers/<slug:slug>/papers-list/<int:pk>/', views.delete_papers, name = "delete_papers"),
    path('profile/', views.edit_user, name = "profile"),
    path('profile/info/', views.info, name = "info"),
    path('<single_slug>/', views.error_page, name = "error_page")
]