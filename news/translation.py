from modeltranslation.translator import translator, TranslationOptions
from news.models import Article, Blog


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Article, ArticleTranslationOptions)


class BlogTranslationOptions(TranslationOptions):
    fields = ('section', 'title', 'text')


translator.register(Blog, BlogTranslationOptions)
