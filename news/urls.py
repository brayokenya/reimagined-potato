from django.urls import include, re_path 
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static
from . import views


urlpatterns=[
    # re_path('^$',views.welcome,name = 'welcome'),
    re_path('^$',views.news_today,name='newsToday'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^article/(\d+)',views.article,name ='article'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    re_path(r'^new/article$', views.new_article, name='new-article'),
    re_path(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    re_path(r'^api/merch/$', views.MerchList.as_view()),
    re_path(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view())

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)