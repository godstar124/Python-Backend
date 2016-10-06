from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title', 'start_date', )


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.question.title + ' ' + self.user.username

    class Meta:
        ordering = ('created_at', )
        unique_together = ('question', 'user', )
