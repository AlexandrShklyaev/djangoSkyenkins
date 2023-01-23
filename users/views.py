from django.views.generic import CreateView

from users.forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = '/'
