from django.db import models
import datetime
from django.utils import timezone

class Category(models.Model):
    type_of_category = models.CharField(max_length=200)
    created_on = models.DateTimeField('created on')


class Result(models.Model):
    category = models.ForeignKey(Category)
    category_result = models.CharField(max_length=200)
    rating = models.DecimalField('', '', 8, 3)
    ratings_count = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    created_by = models.IntegerField(default=0, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.category_result


