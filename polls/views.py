from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
# import models
from .models import Question, Choice
# loader for TEMPLATES
from django.template import loader
# shortcut to load template, fill context and return http - use render
from django.shortcuts import render, get_object_or_404
# create shortcut for get obj or 404
# Create your views here - tomek michalik june
def detail(request, question_id):
    # raise 404 if not in try block
    '''try:  # longer way of raising 404 or getting question obj
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")'''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':
    question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:   # access request.POST = dictionary/json type format sumbitted in post - use to acccess attrib
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form
        return render(request, 'polls/detail.html', { 'question': question,'error_message': "You didnt select a choice",})
    else:
        # add votes increment to models
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # link template from file loc
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context, request))
