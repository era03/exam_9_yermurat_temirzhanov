from django.urls import path, include
from api.views import AddToFavorite



urlpatterns = [
    path('add_to_favorite/<int:pk>', AddToFavorite.as_view(), name='favorite'),
]