from django.shortcuts import render
from django.http import HttpResponse
from notice.models import Notice, Qna

def main(request):
    Main_Notice = Notice.objects.order_by('-id')[0:4] # 메인페이지 게시물 4개 최신순

    return render(request, 'main/main.html', {'MainNotice':Main_Notice})

def search(request):
    return render(request, 'main/Search_result.html')