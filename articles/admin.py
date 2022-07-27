from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    count += 1

        if count != 1:
            raise ValidationError('Нужно указать Один основной раздел')

        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 1
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['title', 'published_at']
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass





# from django.contrib import admin

# from .models import Article, Object, Relationship, ArticleScope


# # class RelationshipInline(admin.TabularInline):
# #     model = Relationship
# #     extra = 2

# class ArticleScopeInline(admin.TabularInline):
#     model = ArticleScope

# @admin.register(Object)
# class ObjectAdmin(admin.ModelAdmin):
#     inlines = [RelationshipInline]

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [ArticleScopeInline]
#     pass