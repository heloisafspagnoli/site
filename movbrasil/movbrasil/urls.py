from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView 

from movBrasil_app.views import pag_inicial_view, quem_somos_view, cursos_view,\
                                getCurso_view, contato_view, contato_efetuado_view

urlpatterns = patterns('',
    url(r'^$', pag_inicial_view, name="home"),
    url(r'^quem_somos/', quem_somos_view, name="quem_somos"),
    url(r'^cursos/', cursos_view, name='cursos'),
    url(r'^cursos/(?P<selected_page>\d+)/?$', cursos_view),
    url(r'^curso/(?P<cursoSlug>[-a-zA-Z0-9]+)/?$', getCurso_view, name='curso_item'),
    url(r'^contato/', contato_view, name="contato"),
    url(r'^contato_efetuado/', contato_efetuado_view, name="contato_efetuado"),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
