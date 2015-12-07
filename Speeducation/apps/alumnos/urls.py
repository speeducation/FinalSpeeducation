from django.conf.urls import include, url
from . import views

urlpatterns = [
    #ALUMNOS
    url(r'^alumnos/lista/$', views.lista_alumnos),
    url(r'^alumno/(?P<pk>[0-9]+)/$', views.detalles_alumno),
    url(r'^alumno/(?P<pk>[0-9]+)/editar/$', views.editar_alumno, name='editar_alumno'),
    url(r'^alumno/agregar/$', views.agregar_alumno, name='agregar_alumno'),
    url(r'^alumno/(?P<pk>[0-9]+)/eliminar/$', views.eliminar_alumno, name='eliminar_alumno'),

    #PLANES DE ESTUDIOS DE UN ALUMNO
    url(r'^alumno/([0-9]+)/plan/(?P<pk>[0-9]+)$', views.detalles_plan, name='detalles_plan'),
    url(r'^alumno/(?P<pk>[0-9]+)/plan/agregar$', views.agregar_plan, name='agregar_plan'),
    url(r'^alumno/([0-9]+)/plan/(?P<pk>[0-9]+)/editar$', views.editar_plan, name='editar_plan'),
    url(r'^alumno/([0-9]+)/plan/(?P<pk>[0-9]+)/eliminar$', views.eliminar_plan, name='eliminar_plan'),

    #EVALUACIONES DE ALUMNO
    url(r'^alumno/([0-9]+)/plan/([0-9]+)/linea/(?P<pk>[0-9]+)/evaluacion/agregar$', views.agregar_evaluacion, name='agregar_evaluacion'),
    url(r'^alumno/([0-9]+)/plan/([0-9]+)/linea/([0-9]+)/evaluacion/(?P<pk>[0-9]+)/eliminar$', views.eliminar_evaluacion, name='eliminar_evaluacion'),
    url(r'^alumno/([0-9]+)/plan/([0-9]+)/linea/([0-9]+)/evaluacion/(?P<pk>[0-9]+)/editar', views.editar_evaluacion, name='editar_evaluacion'),

]
