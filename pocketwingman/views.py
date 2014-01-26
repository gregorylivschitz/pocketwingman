from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import request
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


from pocketwingman.models import Category, Result
from pocketwingman.forms import ResultForm, CategoryForm

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


def help_me(request,category_id):
    latest_result_list = Result.objects.filter(category_id__in=[category_id])
    context = {'latest_result_list': latest_result_list}
    return render(request, 'pocketwingman/help_me.html', context)

def help_out(request, category_id):
    if request.method == 'POST':
        form = ResultForm(request.POST)
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
        form = ResultForm()
    context = {'form': form, 'category_id': category_id}
    return render(request,'pocketwingman/help_out.html', context)

