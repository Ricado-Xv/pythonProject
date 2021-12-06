from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('load_test',views.load_test,name='load_test'),
    path('new_load_test',views.new_load_test, name='new_load_test'),
    path('by_country',views.by_country,name='by_country'),
    path('by_overall',views.by_overall,name='by_overall'),
    path('by_world',views.by_world,name='by_world'),
    path('by_area',views.by_area,name='by_area'),
    path('by_date',views.by_date,name='by_date'),
    path('by_increase',views.by_increase,name='by_increase'),
    path('by_searchterm',views.by_searchterm,name='by_searchterm')
]