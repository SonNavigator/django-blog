from django.urls import path
from .views import index, blog_detail, contact, search, sign_in, sign_in_page, sign_out, sign_up

urlpatterns = [
    # path('url-name', function_name)
    path('', index),
    path('posts/<int:id>', blog_detail),
    path('contact', contact, name="contact"),
    path('search', search),
    # path('sign-in-page', sign_in_page, name="sign-in-page"),
    path('sign-in', sign_in, name="sign-in"),
    path('sign-out', sign_out, name="sign-out"),
    path('sign-up', sign_up, name="sign-up"),


]



