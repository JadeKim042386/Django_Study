from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

def index(request):
    """
    output pybo list
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    output pybo content
    """
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    register answer
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    """
    register question
    """
    #저장하기(POST)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid(): #form 유효성 검사
            question = form.save(commit=False) #임시 저장 (create_date값이 설정되지 않음)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    #질문 등록하기(GET)
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)