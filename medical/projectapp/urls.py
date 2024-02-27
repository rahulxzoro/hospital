from django.urls import path
from . import views

app_name='services'

urlpatterns = [
    path('',views.home,name='home') ,
    path('service/<slug:c_slug>/', views.by_category, name='by_category'),
    path('service/', views.service, name='service'),
]
