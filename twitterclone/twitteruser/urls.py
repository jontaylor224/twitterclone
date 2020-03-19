from django.urls import path
from twitterclone.twitteruser import views as userviews

urlpatterns = [
    path('sign_up/', userviews.Create_New_User.as_view(), name='sign_up'),
    path('users/<int:user_id>/', userviews.UserDetail.as_view(), name='user_detail'),
    path('all_users/', userviews.All_Users.as_view(), name='all_users'),
    path('follow/<int:other_user_id>/', userviews.Follow.as_view(), name='follow'),
    path('unfollow/<int:other_user_id>/', userviews.Unfollow.as_view(), name='unfollow'),
]
