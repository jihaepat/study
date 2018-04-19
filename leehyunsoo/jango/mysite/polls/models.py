from django.db import models
from django.conf import settings
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = True)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text

class Meetup(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=True)
    title = models.CharField(max_length= 200)