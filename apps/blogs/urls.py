from django.urls import path

from . import views


app_name = 'blogs'
urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<int:blog_pk>/', views.blog_detail, name='blog_detail'),
    path('love_blog/', views.love_blog, name='love_blog'),
]
