import django.contrib.auth.models
from django.db import models
from rest_framework.exceptions import ValidationError


class Follows(models.Model):
    follower = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE, related_name='follower')
    leader = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE, related_name='leader')
    subscription_time = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = ('follower', 'leader')
        verbose_name_plural = 'Follows'

    def clean(self):
        follower_id = self.follower.id
        leader_id = self.leader.id
        if follower_id == leader_id:
            raise ValidationError('You cannot follow yourself')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Follows, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.follower.username} - {self.leader.username}'


class CustomUser(models.Model):
    description = models.TextField(null=True)
    user = models.OneToOneField(django.contrib.auth.models.User, on_delete=models.CASCADE, related_name='user')
    subscriptions = models.ManyToManyField('CustomUser', through=Follows, related_name='leader_follower')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=150, null=True)
    content = models.TextField(max_length=5000)
    written_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(null=True)

    custom_user = models.ForeignKey(CustomUser, related_name='post', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.custom_user.user.username} - {self.title or self.id}'
