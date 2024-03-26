"""
URL configuration for ithelper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from monitoring import views

printer_patterns = [
    path('',views.printers),
    path('driver/',views.printer_driver),
    path('on_branch/<int:id>/',views.printers_on_branch),
]

urlpatterns = [
    path("", views.index),
    path("auth/",views.auth),
    path("info/", views.info_page),
    path("monitoring/", views.monitoring),
    path("info/<int:id>/",views.info),
    path("about/", views.about),
    path("contacts/", views.contact),
    path("file/", views.file),
    path("setting/",views.setting),
    path("out/", views.logout),
    path("admin/",admin.site.urls),
    path("printer/", include(printer_patterns)),
]