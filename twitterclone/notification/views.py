from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from twitterclone.notification.models import Notification
from twitterclone.twitteruser.models import TwitterUser

@login_required
def notification_view(request):
    user = TwitterUser.objects.get(user=request.user)
    notifications = Notification.objects.filter(recipient=user, unread=True)
    notification_count = len(notifications)
    for notification in notifications:
        notification.unread = False
        notification.save()

    return render(request, 'twitterclone/notification_list.html', {'user': user, 'notification_count': notification_count, 'notifications': notifications})


