from django.contrib import admin
from django.urls import path, include

# Rebranding Admin Site
admin.site.site_header = 'News Crawler - Admin'
admin.site.site_title = 'News Crawler'
admin.site.index_title = 'Admin Dashboard'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/news', include('news.urls')),
]
