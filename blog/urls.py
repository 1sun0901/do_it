from django.urls import path
from . import views
from .views import PostList, PostDetail

urlpatterns = [
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page),
]