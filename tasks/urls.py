from django.urls import path
from tasks import views
urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<pk>', views.delete, name="delete"),
    path('cross_off/<pk>', views.cross_off, name="cross_off"),
    path('cross_on/<pk>', views.cross_on, name="cross_on"),
    path('edit/<pk>', views.edit, name="edit"),
]