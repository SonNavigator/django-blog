from django.urls import path
from .views import index, blog_detail

urlpatterns = [
    # path('url-name', function_name)
    path('', index),
    path('posts/<int:id>', blog_detail)
]



