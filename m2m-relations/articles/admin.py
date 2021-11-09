from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article
from .models import Tag
from .models import Relationship


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_count = 0
        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data and form.cleaned_data['isMain']:
                if not main_tag_count:
                    main_tag_count += 1
                else:
                    raise ValidationError('error')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)
