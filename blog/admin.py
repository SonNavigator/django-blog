from django.contrib import admin
from .models import Post, Author, Contact

from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title',
              'date_created',
              'date_updated')
    summernote_fields = ('body',)
            

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Contact)

