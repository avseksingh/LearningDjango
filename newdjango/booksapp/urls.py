from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boot', views.bootdemo, name='all'),
    path('allbooks', views.allbooks, name='all'),
    path('lt', views.between, name='between'),
    path('search', views.searchbooks, name='search'),
    path('or', views.searchor, name='searchor'),
    path('aggregates', views.aggregates, name='aggregates'),
    path('form', views.showForm, name='form'),
    path('formone', views.showForm1, name='formdata'),
    path('initial', views.showFormInitial, name='initial'),
]
