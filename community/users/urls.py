from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('files/', views.files, name='files'),
    path('users/', views.users, name='users'),
    path('profile/<int:pk>/', views.profile, name='profile')
]
