from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from .models import Answer, Question, User

from .forms import AnswerForm, LoginForm, QuestionForm, RegisterForm

# Create your views here.
@login_required
def home(request):
    context = {}

    questions = Question.objects.all().order_by('-created_at')
    print(questions)

    context["questions"] = questions
    context['form'] = QuestionForm

    return render(request, 'home.html', context)


def register(request):
    context = {}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = None
            try:
                user = User.objects.get(college_email=form.cleaned_data.get('college_email'))
            except (User.DoesNotExist):
                pass
            
            if user: 
                context["msg"] = "Account already exists!"
            else:
                user = User.objects.create_user(**form.cleaned_data)
                auth_login(request, user)
                return redirect('home')
                
    if request.user.is_authenticated:
        return redirect('home')

    context['form'] = RegisterForm()
    return render(request, 'register.html', context)


def login(request):
    context = {}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            college_email = form.cleaned_data.get('college_email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, college_email=college_email, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                context["msg"] = "Account doesnot exists!"
                
    if request.user.is_authenticated:
        return redirect('home')

    context['form'] = LoginForm()
    return render(request, 'login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def profile(request, id):
    context = {}
    user = None
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponseNotFound()

    context['user'] = user
    return render(request, 'profile.html', context)


@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
        
        return redirect('home')

    return HttpResponseNotFound()


@login_required
def view_question(request, id):
    context = {}
    question = None
    try:
        question = Question.objects.get(id=id)
    except(Question.DoesNotExist):
        return HttpResponseNotFound()

    answers = Answer.objects.filter(question=question)

    context['question'] = question
    context['form'] = AnswerForm()
    context['answers'] = answers
    return render(request, 'question.html', context)



@login_required
def add_answer(request, id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')

            question = None
            try:
                question = Question.objects.get(id=id)
            except(Question.DoesNotExist):
                return HttpResponseNotFound()

            answer = Answer(text=text, user=request.user, question=question)
            answer.save()
        
        return redirect('view_question', id=id)

    return HttpResponseNotFound()
