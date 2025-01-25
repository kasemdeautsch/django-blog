from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
# Register your models here.
class AboutAdmin(SummernoteModelAdmin):

    # list_display = ('title', 'slug', 'status',)
    # search_fields = ['title', 'content']
    # list_filter = ('status', 'created_on')
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
