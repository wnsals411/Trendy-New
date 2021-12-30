from django.shortcuts import render
from django.http import HttpResponse
from notice.models import Notice, Qna
from main.models import search_word
from django.views.generic import ListView
from django.db.models import Q
from django.utils import timezone
import datetime


def main(request):
    # Main_Notice = Notice.objects.order_by('-id')[0:4] # 메인페이지 게시물 4개 최신순
    Hot_QNA = Qna.objects.filter(create_at__gte=timezone.now()-datetime.timedelta(days=7)).order_by('-hits')[0:4]
    # QNA 게시물 조회수 순 4개 (현재날짜부터 7일까지 데이터중)
    Rank = search_word.objects.order_by('-hits')[0:10] # 랭킹 10개 검색횟수 많은순
    time1 = timezone.now()
    time7 = timezone.now()-datetime.timedelta(days=7)
    


    return render(request, 'main/main.html', {
        # 'MainNotice':Main_Notice, 
        'Rank':Rank,
        'HotQNA':Hot_QNA,

        'time1' : time1,
        'time7' : time7,

        })

class SearchView(ListView): # 게시글
    model = search_word
    template_name = 'main/Search_result.html'  

    def get_queryset(self):
        keyword = self.request.GET.get('q', '')
        if keyword:
            
            if search_word.objects.filter(keyword=keyword):
                a = search_word.objects.get(keyword=keyword)
                a.hits += 1
                a.save()
            else:
                b = search_word(keyword=keyword)
                b.save()

        return keyword
    
    
    