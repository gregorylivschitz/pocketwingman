from datetime import datetime

from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, request
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from pocketwingman.models import Category, Result
from pocketwingman.forms import CategoryForm, ResultFormHelpMe, ResultFormHelpOut, UserForm


def index(request):
    return render(request, 'pocketwingman/index.html')


def hard_mode(request):
    if request.method == 'POST':
        request.session['mode'] = 'HARD'
        return HttpResponse()


def easy_mode(request):
    if request.method == 'POST':
        request.session['mode'] = 'EASY'
        return HttpResponse()


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    context = {'user_form': user_form, 'registered': registered}
    return render(request, 'pocketwingman/register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your Pocketwingman account is disabled.")

        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        context = {}
        return render(request, 'pocketwingman/base.html', context)


def help_me(request):
    latest_category_list = Category.objects.all().order_by('id')
    context = {'latest_category_list': latest_category_list}
    return render(request, 'pocketwingman/help_me.html', context)


def help_out(request):
    latest_category_list = Category.objects.all().order_by('id')
    context = {'latest_category_list': latest_category_list}
    return render(request, 'pocketwingman/help_out.html', context)


def help_me_result(request, category_id):
    form = ResultFormHelpMe()

    if request.session.get('mode'):
        mode_type = request.session.get('mode')
    else:
        mode_type = 'EASY'

    if mode_type == 'EASY':
        query = 'select * from (select * from pocketwingman_result where category_id = %s and votes >= 0 order by votes DESC limit (select round(count(*) *.6) ' \
                'from pocketwingman_result where votes >= 0 and category_id = %s)) as qq where category_id = %s order by random() limit 1'

    elif mode_type == 'HARD':
        query = 'select * from (select * from pocketwingman_result where category_id = %s and votes < 0 order by votes DESC limit (select round(count(*) *.6) ' \
                'from pocketwingman_result where votes < 0 and category_id = %s)) as qq where category_id = %s order by random() limit 1'

    params = [category_id, category_id, category_id]
    latest_result_list = Result.objects.raw(query, params)
    context = {'form': form, 'category_id': category_id, 'latest_result_list': latest_result_list,
               'mode_type': mode_type}
    return render(request, 'pocketwingman/help_me_result.html', context)


def help_me_result_post(request, category_id, result_id):
    if request.method == 'POST':
        form = ResultFormHelpMe(request.POST, instance=Result.objects.get(pk=result_id))

        if form.is_valid():

            category = Category.objects.get(id=category_id)

            #Get result object from db
            result_object = Result.objects.get(id=result_id)

            #Get the votes from the result object
            result_votes = result_object.votes

            #Get the views from the result object
            result_views = result_object.views

            form.category = category
            new_category = form.save(commit=False)

            #Add another view
            result_views += 1

            #Add an up the votes from the form
            result_votes = result_votes + new_category.votes

            new_category.category = Category.objects.get(id=category_id)
            new_category.result_votes = result_votes
            new_category.views = result_views
            new_category.save()
            return index(request)

        else:
            print form.errors
    else:
        form = ResultFormHelpMe()
    context = {'form': form, 'category_id': category_id}
    return render(request, 'pocketwingman/help_me_result.html', context)


def help_out_result(request, category_id):
    if request.method == 'POST':
        form = ResultFormHelpOut(request.POST)
        if form.is_valid():


            if request.user.is_authenticated():
                #Get the user who submitted the request
                current_user_id = request.user.id
                user = User.objects.get(id=current_user_id)
                category = Category.objects.get(id=category_id)

                form.category = category
                form.created_by = user
                new_category = form.save(commit=False)
                new_category.category = Category.objects.get(id=category_id)
                new_category.created_by = User.objects.get(id=current_user_id)
                new_category.save()

                return index(request)
            else:
                #Set all anonymous users to 1
                user = User.objects.get(id=1)
                category = Category.objects.get(id=category_id)

                form.category = category
                form.created_by = user
                new_category = form.save(commit=False)
                new_category.category = Category.objects.get(id=category_id)
                new_category.created_by = User.objects.get(id=1)
                new_category.save()

                return index(request)

        else:
            print form.errors
    else:
        form = ResultFormHelpOut()
    context = {'form': form, 'category_id': category_id}
    return render(request, 'pocketwingman/help_out_result.html', context)

