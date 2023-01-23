from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('career/', views.career, name='career'),
    
    path('admin/', admin.site.urls),
    
]