from django.urls import path
from twitterclone.twitteruser import views as userviews

urlpatterns = [
    path('sign_up/', userviews.create_new_user, name='sign_up'),
    path('users/<int:user_id>/', userviews.user_detail, name='user_detail'),
    path('all_users/', userviews.all_users, name='all_users'),
    path('follow/<int:other_user_id>/', userviews.follow, name='follow'),
    path('unfollow/<int:other_user_id>/', userviews.unfollow, name='unfollow'),
]
