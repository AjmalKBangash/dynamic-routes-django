from django.urls import path
from . import views
# from .. import views
from months_dynamic_list import views as notem_views

urlpatterns = [
    path('', views.monthshistory, name="goback"),
    path('months', views.handlereverse, name="reversing" ),
    path('<str:monthsss>', notem_views.monthslist, name="months-description"),

]
