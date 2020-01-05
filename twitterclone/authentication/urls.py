from django.urls import path
# from django.contrib.auth import views as auth_views
from twitterclone.authentication.views import login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]