from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from pocketwingman.models import Category, Result

#class IndexView(generic.ListView):
#    template_name = 'pocketwingman/index.html'
#    context_object_name = 'latest_result_list'

#    def get_queryset(self):
#            """
#            Return the last five categories
#            """
#            #return Category.objects.filter().order_by('-created_on')[:5]
#            return Result.objects.filter()

def index(request):
    latest_result_list = Result.objects.all().order_by('created_on')[:1]
    context = {'latest_result_list': latest_result_list}
    return render(request, 'pocketwingman/index.html', context)

def index(request):
    latest_result_list = Result.objects.all().order_by('created_on')[:1]
    context = {'latest_result_list': latest_result_list}
    return render(request, 'pocketwingman/index.html', context)


def help_me(request,category_id):
    latest_result_list = Result.objects.filter(category_id__in=[category_id])
    context = {'latest_result_list': latest_result_list}
    return render(request, 'pocketwingman/index.html', context)

