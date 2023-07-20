from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/countries/', views.countries_data, name='countries_data'),
    path('api/regions/', views.regions_data, name='regions_data'),
    path('api/relevance/', views.relevance_data, name='relevance_data'),
    path('api/likelihood/', views.likelihood_data, name='likelihood_data'),
    path('api/intensity/', views.intensity_data, name='intensity_data'),
    path('api/year/', views.year_data, name='year_data'),
    path('icons/dashboard', views.dashboard, name='dashboard'),
]
