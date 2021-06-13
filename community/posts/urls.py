from django.urls import path
from posts import views


app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='all'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('new/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('user/', views.UserPostListView.as_view(), name='user_posts')
]
