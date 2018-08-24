from django.conf.urls import url
from data_rest_api import views
from rest_framework.urlpatterns import format_suffix_patterns


# 继承实现
urlpatterns = [
    url(r'^$', views.api_root),
    # url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    # url(r'^users/$', views.UserList.as_view(), name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)

# # 原生/装饰器实现
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
