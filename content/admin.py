from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from parler.admin import TranslatableAdmin
from content.models import NewsModel


class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = NewsModel
        fields = ('text',)


class NewsAdmin(TranslatableAdmin):
    form = NewsAdminForm

    list_display = ('id', 'title',)
    fieldsets = (
        (None, {'fields': ('title', 'text')}),
        )


admin.site.register(NewsModel, NewsAdmin)