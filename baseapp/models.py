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
    follows = models.ManyToManyField('self', through=Follows, symmetrical=False)

    def __str__(self):
        return self.user.username
