from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ..models import Question
from django.db.models import Q

def index(request):
    """
    output pybo list
    """
    #input parameter
    page = request.GET.get('page', '1') #page
    kw = request.GET.get('kw', '')  # 검색어

    #check
    question_list = Question.objects.order_by('-create_date')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    #paging
    paginator = Paginator(question_list, 10) #10 per page
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    output pybo content
    """
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)