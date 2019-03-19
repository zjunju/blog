from django.urls import path

from . import views


app_name = 'utils'
# localhost:8000//comment/
# comment_view  保存评论
urlpatterns = [
    path('', views.comment_viwe, name='comment_view'),
    path('get_reply/', views.get_comment_reply, name='get_comment_reply'),
    path('reply_comment/', views.reply_comment, name='reply_comment'),
]

