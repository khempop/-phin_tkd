from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView, PasswordSetView

class MyPasswordChangeView( PasswordChangeView):
    success_url = reverse_lazy("dashboards:dashboard")


class MyPasswordSetView( PasswordSetView):
    success_url = reverse_lazy("dashboards:dashboard")


# custom 404 view
def custom_404(request, exception):
    return render(request, 'pages/404.html', status=404)

# custom 500 view
def custom_500(request, *args, **argv):
    return render(request, 'pages/500.html', status=500)

