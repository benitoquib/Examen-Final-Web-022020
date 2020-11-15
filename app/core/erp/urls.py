from django.urls import path
from core.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', ProductListView.as_view(), name='category_list'),
    path('category/list2/', product_list, name='category_list2'),
    path('category/add/', ProductCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', ProductUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', ProductDeleteView.as_view(), name='category_delete'),
]
