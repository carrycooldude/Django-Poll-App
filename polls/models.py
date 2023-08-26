from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone
from django.contrib import admin

import uuid

class Question(models.Model):
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now)
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

