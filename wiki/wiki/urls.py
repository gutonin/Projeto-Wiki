from django.conf.urls import url, include
from django.contrib import admin
from materias import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.listagem),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalhe_materia, name='detalhe_materia'),
    url(r'^add_materia$', views.adicao_materia, name='adicao_materia'),
]
