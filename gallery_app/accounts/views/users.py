from django.views.generic import DetailView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from gallery.models import Picture


class UserChangePermissions(UserPassesTestMixin):

    def test_func(self):
        return self.get_object().username == self.request.user or self.request.user.is_superuser

class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        pictures = self.object.favorite_pics.order_by('created_at')
        kwargs['pictures'] = pictures
        return super().get_context_data(**kwargs)