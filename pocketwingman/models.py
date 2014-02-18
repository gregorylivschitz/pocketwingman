from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class Category(models.Model):
    type_of_category = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now=True)


class Result(models.Model):
    category = models.ForeignKey(Category)
    category_result = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, null=True)
    views = models.IntegerField(default=1, null=True)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.category_result


class ResultUser(models.Model):
    voted_by = models.ForeignKey(User)
    category_result = models.ForeignKey(Result)
    down_votes = models.IntegerField(null=True)
    up_votes = models.IntegerField(null=True)
    votes = models.IntegerField(default=0, null=True)
    created_on = models.DateTimeField(auto_now=True)
