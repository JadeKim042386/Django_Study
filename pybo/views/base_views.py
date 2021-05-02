from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ..models import Question

def index(request):
    """
    output pybo list
    """
    #input parameter
    page = request.GET.get('page', '1') #page

    #check
    question_list = Question.objects.order_by('-create_date')

    #paging
    paginator = Paginator(question_list, 10) #10 per page
    page_obj = paginator.get_page(page)

    context = {'question_list' : page_obj}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    output pybo content
    """
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)