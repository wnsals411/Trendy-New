from django.shortcuts import render
from django.http import HttpResponse
from notice.models import Notice, Qna
from main.models import search_word
from django.views.generic import ListView
from django.db.models import Q


def main(request):
    Main_Notice = Notice.objects.order_by('-id')[0:4] # 메인페이지 게시물 4개 최신순
    Rank = search_word.objects.order_by('-hits')[0:10] # 랭킹 10개 검색횟수 많은순

    return render(request, 'main/main.html', {'MainNotice':Main_Notice, 'Rank':Rank})

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
    
    
    