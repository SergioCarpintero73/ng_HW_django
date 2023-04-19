from django.contrib import admin

from .models import Article, Tag, ArticleTag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ArticleTagFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            checked = form.cleaned_data['is_main']
            if checked:
                count += 1
        if count == 0:
            raise ValidationError('Выберите основной раздел')
        elif count > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ArticleTagInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ArticleTagInline, ]