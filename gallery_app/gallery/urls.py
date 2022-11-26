from django.urls import path
from gallery.views import PictureCreateView, PictureDeleteView, PictureDetailView, PictureUpdateView, PicturesView


urlpatterns = [
    path('', PicturesView.as_view(), name='pictures'),
    path('create/', PictureCreateView.as_view(), name='picture_create'),
    path('<int:pk>/detail', PictureDetailView.as_view(), name='picture_detail'),
    path('<int:pk>/update/', PictureUpdateView.as_view(), name='picture_update'),
    path('<int:pk>/delete/', PictureDeleteView.as_view(), name='picture_delete'),
    path('<int:pk>/confirm-delete/', PictureDeleteView.as_view(), name='picture_confirm_delete'),
]