from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag



class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count +=1
            else:
                continue
        if count >= 2:
            raise ValidationError('Основным может быть только один раздел')
        elif count == 0:
            raise ValidationError('Выберите основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 0
    formset = RelationshipInlineFormset



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'published_at', 'image',)
    inlines = [ArticleTagInline]
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ArticleTagInline]



