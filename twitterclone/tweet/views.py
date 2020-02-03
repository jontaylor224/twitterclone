from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from twitterclone.notification.models import Notification
from twitterclone.tweet.forms import TweetForm
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser
import re


@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            content = form_data.get('content')
            user = TwitterUser.objects.get(user=request.user)
            new_tweet = Tweet.objects.create(content=content, author=user)
            new_tweet.save()
            if "@" in content:
                notified_users = re.findall(r"@(\w+)", content)
                if notified_users:
                    for notified_user in notified_users:
                        recipient_user = User.objects.get(username=notified_user)
                        Notification.objects.create(tweet = new_tweet, recipient = TwitterUser.objects.get(user=recipient_user))
            return HttpResponseRedirect('/')

    else:
        form = TweetForm()
    return render(request, 'twitterclone/tweet.html', {'form': form})


def tweet_detail(request, tweet_id):
    tweet = Tweet.objects.get(pk=tweet_id)
    return render(request, 'twitterclone/tweet_detail.html', {'tweet': tweet})

