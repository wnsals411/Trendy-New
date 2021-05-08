from django.contrib import admin
from main.models import search_word
# Register your models here.


class search_wordAdmin(admin.ModelAdmin):
    fields = ['keyword', 'hits']
    list_display = ('keyword', 'hits')


admin.site.register(search_word, search_wordAdmin)

