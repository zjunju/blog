import xadmin

from .models import Comment


class CommentAdmin(object):
    list_display = ['pk','auth', 'content', 'date_time']
    list_filter = ['auth', 'date_time']


xadmin.site.register(Comment, CommentAdmin)
