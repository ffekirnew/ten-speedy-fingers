from django.db import models
from datetime import datetime
# Create your models here.

class TestText(models.Model):
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.title

class Test(models.Model):
    test_text = models.ForeignKey(TestText, on_delete=models.CASCADE)
    taken_date = models.DateTimeField('test taken on date')
    wpm = models.IntegerField('words per minute')
    accuracy = models.IntegerField('accurate words')

    def __str__(self) -> str:
        return "{} on date {}".format(self.test_text, self.taken_date)