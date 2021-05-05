from django import template
import markdown
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter()
def mark(value):
    '''
    nl2br : 줄바꿈 문자를 <br> 태그로 바꿔 줌
    fenced_code : 마크다운의 소스 코드 표현을 위해 적용
    '''
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))