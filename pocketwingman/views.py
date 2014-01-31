from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import request, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import random

from pocketwingman.models import Category, Result
from pocketwingman.forms import CategoryForm, ResultFormHelpMe, ResultFormHelpOut

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
    return render(request, 'pocketwingman/index.html')

def help_me(request):
    latest_category_list = Category.objects.all().order_by('id')
    context = {'latest_category_list': latest_category_list}
    return render(request, 'pocketwingman/help_me.html', context)

def help_out(request):
    latest_category_list = Category.objects.all().order_by('id')
    context = {'latest_category_list': latest_category_list}
    return render(request, 'pocketwingman/help_out.html', context)


def help_me_result(request,category_id):
    if request.method == 'POST':
        form = ResultFormHelpMe(request.POST)

        if form.is_valid():

            category = Category.objects.get(id=category_id)
            form.category = category
            new_category = form.save(commit=False)
            new_category.category = Category.objects.get(id=category_id)
            new_category.save()

            return index(request)

        else:
            print form.errors
    else:
        form = ResultFormHelpMe()
    latest_result_list = Result.objects.raw('select * from pocketwingman_result where id=1 and category_id = ')
    context = {'form': form, 'category_id': category_id,'latest_result_list': latest_result_list}
    return render(request,'pocketwingman/help_me_result.html', context)


def help_out_result(request, category_id):
    if request.method == 'POST':
        form = ResultFormHelpOut(request.POST)
        if form.is_valid():

            category = Category.objects.get(id=category_id)
            form.category = category
            new_category = form.save(commit=False)
            new_category.category = Category.objects.get(id=category_id)
            new_category.save()

            return index(request)

        else:
            print form.errors
    else:
        form = ResultFormHelpOut()
    context = {'form': form, 'category_id': category_id}
    return render(request,'pocketwingman/help_out_result.html', context)

