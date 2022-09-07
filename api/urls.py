from django.urls import path, include

urlpatterns = [
    path('qlpt', include('qlpt.api.urls')),
    # path('phuongtien', include('PT.api.urls')),
    path('user', include('profiles.api.urls')),
    path('coso', include('coso.api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
]
