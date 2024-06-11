from django.urls import path
from . import views


urlpatterns = [
    path('favourites_list/', views.favourites_list, name='favourites_list'),
    path('delete_your_blog/<int:pk>/', views.delete_blog, name='delete'),
    path('favourites/<int:id>/', views.favourites, name='favourites'),
    path('edit_your_blog/<int:pk>/', views.edit_blog, name='edit'),
    path('details/<str:pk>/', views.detail, name='details'),
    path('add_your_blog/', views.add_blog, name='add'),
    path('search/', views.search, name='search'),
    path('', views.blog, name='blogs'),
]
