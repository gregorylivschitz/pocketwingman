from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from pocketwingman.models import Category, Result

class IndexView(generic.ListView):
    template_name = 'pocketwingman/index.html'
    context_object_name = 'latest_result_list'

    def get_queryset(self):
            """
            Return the last five categories
            """
            #return Category.objects.filter().order_by('-created_on')[:5]
            return Result.objects.filter()