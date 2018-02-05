from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question, InterestedPerson
from .forms import EmailForm
from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['to@example.com'],
#     fail_silently=False,
# )


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list': latest_question_list}
#     return HttpResponse(template.render(context, request))


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    heading_0 = dict(title='AeroPress XL',
                     blurb="""Use the AeroPress with Wide Mouth Mugs"""
                     )
    heading_1 = dict(title='Fits perfectly on large size mugs',
                     blurb="""Examples:  Github Mug, Life is Good Mug, etc."""
                     )
    heading_2 = dict(title='Simple Integration',
                     blurb="""Just place on top of your mug, and use the AeroPress as normal."""
                     )

    company = dict(name='AeroPress Extendz',
                   vision=''
                   )

    context = dict(company=company,
                   heading=[heading_0, heading_1, heading_2],
                   form=form)

    # print(form)

    return render(request, 'marketing/index.html', context)


def thanks(request):
    context = {}
    return render(request, 'marketing/thanks.html', context)


def pricing(request):
    context = {}
    return render(request, 'marketing/pricing.html', context)


def cart(request):
    context = {}
    return render(request, 'marketing/cart.html', context)


def get_email(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    context = {'form': form}
    print(context)

    return render(request, 'marketing/form.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'marketing/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
