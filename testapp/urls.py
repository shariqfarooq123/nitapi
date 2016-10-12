"""nit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
   url(r'^subjects/([b,m,p]_[A-Z]{3}_[0-8]_[0-9]{2})/assignments/upload/([A-Za-z]{1,30})/$',views.handle_upload_assignment),
   url(r'^subjects/([b,m,p]_[A-Z]{3}_[0-8]_[0-9]{2})/notes/upload/([A-Za-z]{1,30})/$',views.handle_upload_notes),
   url(r'^subjects/([b,m,p]_\w*)/assignments/$',views.get_assigns),
   url(r'^subjects/([b,m,p]_\w*)/$',views.get_subs_of_sem),
   url(r'^subjects/([b,m,p]_\w*)/notes/$',views.get_notes),
]
