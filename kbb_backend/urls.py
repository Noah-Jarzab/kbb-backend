from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('shoes', views.ShoeList.as_view(), name='shoe_list'),
    path('shoes/<int:pk>', views.ShoeDetail.as_view(), name='shoe_detail'),
    path('collections', views.CollectionList.as_view(), name='collection_list'),
    path('collections/<int:pk>', views.CollectionDetail.as_view(), name='collection_detail')
]