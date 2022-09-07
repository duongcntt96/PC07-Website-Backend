
from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test', index),
    # path('', include('home.urls')),
    # path('person/', include('person.urls')),
    path('docs/', include('docs.urls')),
    # path('phuongtien/', include('PT.urls')),
    path('api/', include('api.urls')),
    # path('api/', include('profiles.api.urls')),
]
