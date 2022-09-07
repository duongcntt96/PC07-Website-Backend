from django.urls import path
from . import views
app_name = "home"
urlpatterns = [
   path('home/', views.index, name="index"),
   path('contact/', views.contact, name="contact"),
   path('about/', views.about, name="about"),
   path('law/', views.law, name="law"),
   path('feedback/',views.feedback, name="feedback"),
   path('<int:id>/', views.post, name="post")
]