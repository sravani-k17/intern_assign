from django.urls import path,include,re_path
from . import views
from .views import index,result,display
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    re_path('^$', index, name='index'),
    path('result/',result,name='result'),
    path('display/',display,name='display')
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
