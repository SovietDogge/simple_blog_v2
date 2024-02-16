import django.contrib.auth.models
from django.db import models


class Followers(models.Model):
    follower = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE, related_name='follower')
    leader = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE, related_name='leader')

    class Meta:
        unique_together = ('follower', 'leader')

    def __str__(self):
        return f'{self.follower.username} - {self.leader.username}'


class CustomUser(models.Model):
    registered_time = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.TextField(null=True)
    user = models.OneToOneField(django.contrib.auth.models.User, on_delete=models.CASCADE, related_name='user')
    subscriptions = models.ManyToManyField('CustomUser', through=Followers, related_name='leader_follower')

    def __str__(self):
        return self.user.username
