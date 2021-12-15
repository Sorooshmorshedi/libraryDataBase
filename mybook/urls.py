from django.contrib import admin
from django.urls import path 
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from tp_book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tp_book.urls')),
    path('', include('tp_book.urls')),
    path('', views.index, name='index'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	
