from django.contrib import admin
from news.models import Article, Blog
from modeltranslation.admin import TranslationAdmin


class NewsAdmin(TranslationAdmin):
    pass


class BlogAdmin(TranslationAdmin):
    pass


admin.site.register(Article, NewsAdmin)
admin.site.register(Blog, BlogAdmin)
