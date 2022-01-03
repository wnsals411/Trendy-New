from django.urls import path
from . import views

app_name = 'notice'
urlpatterns = [
    path('', views.main, name = 'main'),
    path('qna/', views.QnaListView.as_view(), name = 'qna'), # Q&A 리스트 페이지
    path('qna=notice/', views.qnanotice, name = 'qnanotice'), # Q&A 작성시 유의사항
    path('qna=<int:pk>/', views.qnadet, name = 'qnadet'), # Q&A 해당 번호 디테일
    path('qna=<int:pk>/delete', views.qnadel, name = 'qnadel'), # Q&A 해당 번호 삭제 (비밀번호 입력 및 POST 메소드)
    path('notice/', views.NoticeListView.as_view(), name='notice'), # 공지사항 리스트
    path('notice=<int:pk>/', views.notdet, name = 'notdet'), # 공지사항 해당 번호 디테일
    path('write/', views.write, name = 'write'), # Q&A 작성
]
