from django.views import View
from django.shortcuts import get_object_or_404
from gallery.models import Picture
from django.http import HttpResponse


class AddToFavorite(View):
    picture_object = None

    def dispatch(self, request, *args, **kwargs):
        self.picture_object = get_object_or_404(Picture, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        users_favorite = self.picture_object.favorite.values_list('id', flat=True)
        print(users_favorite)

        if request.user.pk in users_favorite:
            self.remove_favorite()
        else:
            self.add_favorite()
        return HttpResponse(status=200)

    def add_favorite(self):
        self.picture_object.favorite.add(self.request.user)
    
    def remove_favorite(self):
        self.picture_object.favorite.remove(self.request.user)


