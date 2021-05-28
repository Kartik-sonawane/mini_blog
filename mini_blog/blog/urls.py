from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('addpost/', views.Add_Post, name='addpost'),
    path('updatepost/<int:id>/', views.Update_Post, name='updatepost'),
    path('delete/<int:id>/', views.Delete_Post, name='deletepost'),
]