from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^cursos/', TemplateView.as_view(template_name="cursos.html"), name="cursos")
)
