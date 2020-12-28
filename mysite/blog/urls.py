from django.urls import (
    path,
    re_path,
    include
)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from blog import views


app_name = 'blog'
urlpatterns = [
    path('editorjs/', include('django_editorjs_fields.urls')),
    path('', views.PostLV.as_view(), name='index'),
    re_path(r'^post/(?P<slug>[-\w]+)/$',
            views.PostDV.as_view(),
            name='post_detail'),
    path('categories/<str:category>/',
         views.ObjectsByCategoryLV.as_view(),
         name='object_list_by_category'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)