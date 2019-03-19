import xadmin
from xadmin import views

from .models import Tags, Blog, ReadDetail

class GlobalSettings(object):
    site_title = '大学本科毕业设计管理系统'  #设置网站的title
    site_footer = '玉林师范学院'            #设置网站的footer
    menu_style = 'accordion'               #设置左边的图标样式为折叠

class BlogAdmin(object):
    list_display = ['title']


class TagsAdmin(object):
    list_diplay = ['tag_name', 'date_join']


xadmin.site.register(Tags, TagsAdmin)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
