from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user, name='register'),
    path('', login_view, name='login'),
    # path("account_setting/<user_id>/", account_setting_view, name="account_setting"),
    path('logout/', logout_view, name='logout'),
    path('profile',profile_view,name='profile'),

]
