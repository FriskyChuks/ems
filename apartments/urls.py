from django.urls import path
from .views import *


urlpatterns=[
    path('', home, name='home'),
    path('create_apartment/',create_apartment_view,name='create_apartment'),
    path('apartment_list/',apartment_list_view,name='apartment_list'),
    path('add_occupant/<int:id>/',add_occupant_view,name='add_occupant'),
]