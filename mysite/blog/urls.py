from django.urls import path


from . import views
from .models import Article

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:id>', views.article, name='article'),
    path('contact/', views.contact, name='contact'),
]