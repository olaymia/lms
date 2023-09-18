from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Topic, Question, Choice


@login_required
def select_topic(request):
    topics = Topic.objects.all()
    return render(request, 'toptwo/select_topic.html', {'topics': topics})


@login_required
def select_topic_quantity(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    return render(request, 'toptwo/select_topic_quantity.html', {'topic': topic})


@login_required
def start_topic_quiz(request, topic_id, num_questions):
    topics = Topic.objects.get(id=topic_id)
    questions = Question.objects.filter(id=topic_id).order_by('?')[:num_questions]
    choices = Choice.objects.filter(question__in=questions)
    return render(request, 'toptwo/start_topic_quiz.html', {'topics': topics, 'questions': questions, 'choices': choices})



