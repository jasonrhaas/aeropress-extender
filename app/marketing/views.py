from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question, InterestedPerson
from .forms import EmailForm
from django.core.mail import send_mail


def submit(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = EmailForm()

    context = dict(form=form)

    return render(request, 'marketing/form.html', context)


def index(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')

    else:
        form = EmailForm()

    heading_0 = dict(title='JumboBrew',
                     blurb="""An AeroPress Adapter to use with Wide Mouth Mugs"""
                     )
    heading_1 = dict(title='Fits perfectly on large size mugs',
                     blurb="""Examples:  Github Mug, Starbucks Mug, and more."""
                     )
    heading_2 = dict(title='Simple Integration',
                     blurb="""Just place on top of your mug, and use the AeroPress as normal."""
                     )

    company = dict(name='JumboBrew',
                   vision=''
                   )

    context = dict(company=company,
                   heading=[heading_0, heading_1, heading_2],
                   form=form,
                   )

    # print(form)

    return render(request, 'marketing/index.html', context)


def thanks(request):
    context = {}
    return render(request, 'marketing/thanks.html', context)


def pricing(request):
    if request.method == 'POST':
        print(request.POST)
        form = EmailForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = EmailForm()

    context = dict(form=form)

    return render(request, 'marketing/pricing.html', context)


def cart(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = EmailForm()

    context = dict(form=form)

    return render(request, 'marketing/cart.html', context)
