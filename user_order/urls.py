from django.urls import path
from .views import ShopViewSets, OrderViewSets

urlpatterns = [
    path('shop',ShopViewSets.as_view({
    'get':'list',
    'post': 'create'
    })),
    path('shop/<str:pk>', ShopViewSets.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
    path('order',OrderViewSets.as_view({
    'get':'list',
    'post': 'create'
    })),
    path('order/<str:pk>', OrderViewSets.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }))

]