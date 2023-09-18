from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Subject, Question, Choice, UserResponseParaSub

@login_required
def select_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'subtwo/select_subject.html', {'subjects': subjects})



@login_required
def select_quantity(request, subject_id):
    subject = Subject.objects.get(id=subject_id)

    if request.method == 'POST':
        num_questions = int(request.POST.get('num_questions'))
        if num_questions < 1:
            # Handle invalid input, e.g., show an error message
            return render(request, 'subtwo/select_quantity.html', {'subject': subject})

        # Store num_questions in the session
        request.session['num_questions'] = num_questions

        # Redirect to the start_quiz view
        return redirect('start_quiz', subject_id=subject_id)

    return render(request, 'subtwo/select_quantity.html', {'subject': subject})


@login_required
def start_quiz(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    # Check if the user has already started the quiz
    if 'question_index' not in request.session:
        request.session['question_index'] = 0  # Initialize question index
        request.session['subject_id'] = subject_id  # Store subject ID in session

    # Get the current question index
    question_index = request.session['question_index']

    # Retrieve the questions related to the subject
    questions = Question.objects.filter(subject=subject).order_by('?')

    # Check if there are questions left to display
    if question_index < len(questions):
        current_question = questions[question_index]
        request.session['question_index'] += 1  # Move to the next question
        return render(request, 'subone/start_quiz.html', {
            'subject': subject,
            'current_question': current_question,
        })
    else:
        # All questions have been answered, you can redirect to a completion page or take some other action
        return redirect('quiz_complete')  # Replace 'quiz_complete' with the URL for the completion page
    


@login_required
def submit_quiz(request):
    if request.method == 'POST':
        # Get the submitted question ID and selected answer
        question_id = request.POST.get('question_id')
        selected_answer = request.POST.get('answer')

        # Retrieve the question object
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            # Handle the case where the question does not exist
            return redirect('quiz_complete')  # Redirect to the completion page or take appropriate action

        # Compare the selected answer with the correct answer
        if selected_answer == question.correct_answer:
            # Handle the correct answer scenario (e.g., update the user's score)
            # You can store user answers and scores as needed
            # Handle the incorrect answer scenario (if necessary)

    # Redirect to the next question or the completion page
         return redirect('start_quiz', subject_id=request.session.get('subject_id'))



@login_required
def complete_quiz(request):
    # Retrieve user responses for the quiz
    user_responses = UserResponse.objects.filter(user=request.user)
    
    # Calculate the user's score
    total_questions = user_responses.count()
    correct_answers = user_responses.filter(is_correct=True).count()
    
    # Calculate the result percentage
    if total_questions > 0:
        result_percentage = (correct_answers / total_questions) * 100
    else:
        result_percentage = 0
    
    return render(request, 'subtwo/quiz_complete.html', {
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'score': correct_answers,  # You can use a different scoring system if needed
        'result_percentage': result_percentage,
    })
