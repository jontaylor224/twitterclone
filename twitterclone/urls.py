"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from . import views
from twitterclone.authentication.urls import urlpatterns as auth_urls
from twitterclone.notification.urls import urlpatterns as notification_urls
from twitterclone.twitteruser.urls import urlpatterns as user_urls
from twitterclone.tweet.urls import urlpatterns as tweet_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
]

urlpatterns.extend(auth_urls)
urlpatterns.extend(notification_urls)
urlpatterns.extend(user_urls)
urlpatterns.extend(tweet_urls)
