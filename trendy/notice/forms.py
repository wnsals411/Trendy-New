from django import forms
from notice.models import Qna

class WriteForm(forms.ModelForm):
    
    class Meta:
        model = Qna

        fields = ['title', 'author', 'content', 'image', 'password']
        labels = {
            'title': "Title",
            'author': 'Writer',
            'content': '',
            'image': '이미지첨부',
            'password': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'제목', 'class': 'title', 'size':'29'}),
            'author': forms.TextInput(attrs={'placeholder':'이름', 'class': 'author', 'size':'28'}),
            'content': forms.Textarea(attrs={'placeholder':'내용 최대xx자', 'size': '40', 'rows': '10', 'class': 'content','cols':'37'}),
            'password': forms.PasswordInput(attrs={'placeholder':'비밀번호', 'class': 'password'}),
        }          