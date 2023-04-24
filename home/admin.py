from django.contrib import admin
from .models import Post, Comentarios, Curtidas
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = {'conteudo_post',}


admin.site.register(Post, PostAdmin)
admin.site.register(Comentarios)
admin.site.register(Curtidas)
