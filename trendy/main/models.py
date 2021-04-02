from django.db import models

class search_word(models.Model):  
    keyword = models.CharField(max_length = 50) # 검색단어
    hits = models.IntegerField(default = 1) # 조회수

    def __str__(self):
        return self.keyword