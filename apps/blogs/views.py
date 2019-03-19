from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import ObjectDoesNotExist

from .models import Blog

from apps.utils.restfulAPI import restful

from datetime import datetime, timedelta


class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.prefetch_related('tags').all()

        return render(request, 'blogs/blog_list.html', {'blogs': blogs})

@require_GET
def blog_detail(request, blog_pk):
    try:
        blog = Blog.objects.prefetch_related('tags').get(pk = blog_pk)
        pre_blog = Blog.objects.filter(pub_time__gt=blog.pub_time).last()
        next_blog = Blog.objects.filter(pub_time__lt=blog.pub_time).first()
        context = {}
        context['blog'] = blog
        context['comments'] = blog.comments.select_related('auth').all()
        context['pre_blog'] = pre_blog
        context['next_blog'] = next_blog
        pk = blog.pk
        key = 'read_blog_%s' % (pk)
        read_blog = request.COOKIES.get(key, None)
        if read_blog is None:
            blog.read_times += 1
            blog.save()
            response = render(request, 'blogs/blog_detail.html', context)
            response.set_cookie(key, True)
            return response
        else:
            return render(request, 'blogs/blog_detail.html', context)

    except ObjectDoesNotExist:
        return redirect(reverse('blogs:blog_list'))


@require_GET
def love_blog(request):
    blog_pk = request.GET.get('blog_pk', None)
    if blog_pk:
        try:
            blog = Blog.objects.get(pk=int(blog_pk))
            key = 'loved_blog_%s'%blog_pk
            is_loved = request.COOKIES.get(key, False)
            if is_loved:
                # 判断用户当前点赞的博客是已经点赞过，如果点赞过则直接返回response
                message = '您已经点赞过了， 谢谢你的点赞!'
                return restful.do_nothing(message=message)
                # 如果没有点赞过，则点赞成功, 并且把点赞的博客pk加入到cookies中
            else:
                blog.love += 1
                blog.save()

            current_time = datetime.now()
            tomorrow = current_time + timedelta(days=1)
            reponse = restful.ok()
            reponse.set_cookie(key, True, expires=tomorrow)
            return reponse

        except (ValueError, ObjectDoesNotExist):
            return restful.params_error('没有找到该博客!')

