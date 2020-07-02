from django.urls import path
from . import views
app_name = 'playground' 

urlpatterns = [
    path('', views.index, name='index'),
    path('item/add/', views.add_item, name='add_item'),
    path('item/<uuid:item_id>/read/', views.read_item, name='read_item'),
    path('item/<uuid:item_id>/update/', views.update_item, name='update_item'),
    path('logout/', views.ac_logout, name='logout'),
]