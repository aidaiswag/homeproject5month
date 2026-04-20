from django.urls import path 
from . import views

urlpatterns =[
    path('', views.ProductListAPIView.as_view() ),
    path('<int:id>/', views.ProductDetailAPIView.as_view()),
    path('categories/', views.CategoryViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('categories/<int:id>/', views.CategoryViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('reviews/', views.ReviewViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('reviews/<int:id>/', views.ReviewViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),    
]