from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser


def create_new_user(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data
            username = form_data.get('username')
            new_password = form_data.get('password1')
            user = authenticate(username=username, password=new_password)

            new_user = TwitterUser(user=user)
            new_user.save()

            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'twitterclone/sign_up.html', {'form': form})


@login_required
def follow(request, other_user_id):
    user = TwitterUser.objects.get(user=request.user)
    user_to_follow = TwitterUser.objects.get(pk=other_user_id)
    user.follows.add(user_to_follow)
    user.save()
    return HttpResponseRedirect('/')


def unfollow(request, other_user_id):
    user = TwitterUser.objects.get(user=request.user)
    user_to_unfollow = TwitterUser.objects.get(pk=other_user_id)
    user.follows.remove(user_to_unfollow)
    user.save()
    return HttpResponseRedirect('/')


def all_users(request):
    user_list = TwitterUser.objects.all()
    return render(request, 'user_list.html', {'user_list': user_list})


def user_detail(request, user_id):
    current_user = TwitterUser.objects.get(pk=user_id)
    tweets = Tweet.objects.filter(author=current_user)[::-1]
    tweet_count = len(tweets)
    follows_list = current_user.follows.all()
    follow_count = len(current_user.follows.all())
    context = {'current_user': current_user,
               'tweets': tweets,
               'tweet_count': tweet_count,
               'follow_count': follow_count,
               'follows_list': follows_list}
    return render(request, 'twitterclone/user_detail.html', context)
