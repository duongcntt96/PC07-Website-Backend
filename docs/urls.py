from django.urls import path
from . import views
app_name = "home"
urlpatterns = [
    # path('', views.doc),
    # path('<int:id>', views.doc),
    path('view/<int:id>', views.docx_viewer)
]
