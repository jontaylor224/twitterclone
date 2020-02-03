from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from twitterclone.notification.models import Notification
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser


@login_required
def index(request):
    current_user = TwitterUser.objects.get(user=request.user)
    user_list = TwitterUser.objects.all().exclude(user_id=current_user.user_id)
    user_tweets = Tweet.objects.filter(author=current_user)
    tweet_count = len(user_tweets)
    follows_list = current_user.follows.all()
    follow_count = len(follows_list)
    follows_tweet_list = []
    if follow_count:
        for follow in follows_list:
            follows_tweet_list += Tweet.objects.filter(author=follow)
    follows_tweet_list += user_tweets
    follows_tweet_list = sorted(follows_tweet_list, key= lambda tweet: tweet.time_created, reverse=True)

    notifications_list = Notification.objects.filter(recipient=current_user, unread=True)
    notification_count = len(notifications_list)

    context = {'current_user': current_user,
               'follows_list': follows_list,
               'follows_tweet_list': follows_tweet_list,
               'follow_count': follow_count,
               'user_list': user_list,
               'notifications_list': notifications_list,
               'notification_count': notification_count,
               'tweet_count': tweet_count}
    return render(request, 'twitterclone/index.html', context)