from django.urls import path
from .views import HomeView, MenuView, GalleryListView, FoodTimingView, FoodContactView

app_name = 'foodapp'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('menu/', MenuView.as_view(), name='menu_food'),
    path('gallery/', GalleryListView.as_view(), name='gallery_food'),
    path('timing/', FoodTimingView.as_view(), name='food_timing'),
    path('contact/', FoodContactView.as_view(), name='food_contact'),
]
