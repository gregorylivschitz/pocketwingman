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
    form = ResultFormHelpMe()
    query = 'select * from (select * from pocketwingman_result where category_id = %s and rating >= 3 order by rating DESC limit (select round(count(*) *.6) from pocketwingman_result where rating >= 3 and category_id = %s)) as qq where category_id = %s order by random() limit 1'
    params = [category_id,category_id,category_id]
    latest_result_list = Result.objects.raw(query, params)
    context = {'form': form, 'category_id': category_id, 'latest_result_list': latest_result_list}
    return render(request,'pocketwingman/help_me_result.html', context)

def help_me_result_post(request, category_id, result_id):
    if request.method == 'POST':
        form = ResultFormHelpMe(request.POST, instance=Result.objects.get(pk =result_id))

        if form.is_valid():

            category = Category.objects.get(id=category_id)

            #Get result object from db
            result_object = Result.objects.get(id=result_id)

            #Get the votes from the result object
            result_votes = result_object.votes

            #Get the ratings count from the result object
            ratings_count = result_object.ratings_count

            #Get the rating from the result object
            rating = result_object.rating

            #multiple out the rating and rating_count
            rating_calculated = ratings_count * rating


            form.category = category
            new_category = form.save(commit=False)

            #Add new rating
            rating_calculated = new_category.rating + rating_calculated

            #Add another rating
            ratings_count += 1

            #Add a vote if the current rating is 3 or higher
            if new_category.rating >= 3:
                result_votes = result_votes + 1

            #Calculate the correct rating
            rating_correct = rating_calculated / ratings_count

            new_category.category = Category.objects.get(id=category_id)
            new_category.ratings_count = ratings_count
            new_category.rating = rating_correct
            new_category.votes = result_votes
            new_category.save()
            return index(request)

        else:
            print form.errors
    else:
        form = ResultFormHelpMe()
    context = {'form': form, 'category_id': category_id}
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

