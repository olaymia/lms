from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Semester, Question, Choice


@login_required
def select_semester(request):
    semesters = Semester.objects.all()
    return render(request, 'modtwo/select_semester.html', {'semesters': semesters})


@login_required
def select_semester_quantity(request, semester_id):
    semesters = get_object_or_404(Semester, id=semester_id)
    return render(request, 'modtwo/select_semester_quantity.html', {'semesters': semesters})


@login_required
def start_semester_quiz(request, semester_id, num_questions):
    semesters = Semester.objects.get(id=semester_id)
    questions = Question.objects.filter(id=semester_id).order_by('?')[:num_questions]
    choices = Choice.objects.filter(question__in=questions)
    return render(request, 'modtwo/start_semester_quiz.html', {'semesters': semesters, 'questions': questions, 'choices': choices})


