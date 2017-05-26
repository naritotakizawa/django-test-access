from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic

class HomeView(UserPassesTestMixin, generic.TemplateView):
    template_name = 'app/home.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False