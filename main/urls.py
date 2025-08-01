
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('cv', views.cv, name="cv"),
    path('products', views.products, name='products-list'),
    path('contact_me', views.contact, name = "contact"),
    path('download/<str:filename>/', views.download_file, name='download_file'),
    
    path('blog', views.blog, name='blog'),
    
    # Functionality for the blog-detail
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]
