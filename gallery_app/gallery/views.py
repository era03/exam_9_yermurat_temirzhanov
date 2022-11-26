from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from gallery.models import Picture
from gallery.forms import PictureForm



class PicturesView(ListView):
    template_name = 'pictures.html'
    model = Picture
    context_object_name = 'pictures'
    ordering = ('-created_at',)


class PictureDetailView(DetailView):
    template_name = 'picture_detail.html'
    model = Picture
    context_object_name = 'picture'


class PictureCreateView(CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'picture_create.html'

    def get_success_url(self):
        return reverse('pictures')

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            description = form.cleaned_data.get('description')
            picture = form.cleaned_data.get('picture')
            Picture.objects.create(author=author, picture=picture, description=description)
        return redirect('pictures')
        

class PictureUpdateView(UpdateView):
    template_name = 'picture_edit.html'
    form_class = PictureForm
    model = Picture
    context_object_name = 'picture'

    def get_success_url(self):
        return redirect('picture_detail', pk=self.get_object.pk)


class PictureDeleteView(DeleteView):
    template_name = 'picture_confirm_delete.html'
    model = Picture
    success_url = reverse_lazy('pictures')
    context_object_name = 'picture'
