from django.shortcuts import render, reverse, redirect
from django.views.decorators.http import require_POST, require_GET
from django.template.defaultfilters import escape
from django.core.exceptions import ObjectDoesNotExist

from .restfulAPI import restful
from .decorators import authenticate_user
from .models import Comment
from .forms import CommentForm
from apps.blogs.models import Blog


# 保存评论内容
@require_POST
def comment_viwe(request):
    user = request.user
    if user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            blog_pk = request.POST.get('blog_pk')
            excape_content = escape(content)
            username = user.username
            user_pk = user.pk
            try:
                blog = Blog.objects.get(pk = blog_pk)
                Comment.objects.create(auth=user, content=excape_content, blog=blog)
                return restful.result(data={'content': excape_content,'username': username,'user_pk': user_pk})
            except Exception as e:
                print(e)
                return restful.do_nothing(message='未知错误！')
        else:
            return restful.params_error(message='内容不能为空')
    else:
        return restful.un_signup(message='请先登录！')


@require_GET
def get_comment_reply(request):
    root_comment_pk = request.GET.get('root_comment_pk')
    try:
        comment = Comment.objects.get(pk = root_comment_pk)
        son_comments = comment.root_comment.all()
        if son_comments:
            context = {}
            for each_comment in son_comments:
                context[each_comment.auth.username] = [each_comment.content, each_comment.date_time]
            # context['son_comments'] =serializers.serialize('json',son_comments)
            print(context)
            return restful.result(data=context)
        else:
            return restful.do_nothing(message='该评论暂无回复！')

    except ObjectDoesNotExist:
        return restful.do_nothing(message='该评论不存在或已经删除！')


@require_POST
@authenticate_user
def reply_comment(request):
    # 回复的comment_id 回复的user_id 回复内容
    comment_id = request.POST.get('comment_id')
    user = request.user
    content = request.POST.get('content')
    try:
        parent_comment = Comment.objects.get(id=comment_id)
        root_comemnt = parent_comment.root or parent_comment
        try:
            Comment.objects.create(parent=parent_comment, root=root_comemnt, auth=user, reply_auth=parent_comment.auth, content=content, blog=parent_comment.blog)
            return restful.ok()
        except Exception as e:
            print(e)
            print(type(e))
            return restful.internal_error(message=e)
    except ObjectDoesNotExist:
        return restful.do_nothing(messag='没有找到该篇博客!')
