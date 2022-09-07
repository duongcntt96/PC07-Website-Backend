from django.urls import path
from . import views
app_name = "phuongtien"
urlpatterns = [
   path('', views.index, name="index"),
   path('ten/', views.list_ten, name="ten"),
   path('chungloai/', views.list_chung_loai, name="chungloai"),
   path('to/', views.list_to, name="to"),
   path('noibotri/', views.list_noi_bo_tri, name="noibotri"),
   path('<int:id>/', views.info, name="info"),
   path('<int:id>/add', views.add, name="add"),
   path('search/', views.search, name="search"),
   path('<int:id>/edit', views.edit, name="edit"),
]