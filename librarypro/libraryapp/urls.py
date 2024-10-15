from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login),
    path('SignUp/', views.SignUp),
    path('mainpage', views.mainpage),
    path('profile', views.profile),
    path('about', views.about),
    path('', views.homepage),
    path('books/', views.book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)