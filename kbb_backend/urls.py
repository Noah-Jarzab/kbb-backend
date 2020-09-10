from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('shoes', views.ShoeList.as_view(), name='shoe_list'),
    path('shoes/<int:pk>', views.ShoeDetail.as_view(), name='shoe_detail')
]