from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
# need a form to support the signup
from . import forms
# Create your views here.

# the user creation form is inhereted form the form form form page
# cause we need modify
class SignUp(CreateView):
    # form the forms in the function os UCF
    form_class = forms.UserCreateForm
    # if good return to login/ reverse lazy ensurse it happena after hit the
    # submission buttern
    success_url = reverse_lazy("login")
    # the page show the sign up---the format for all the views
    # current dir/templates/....
    template_name = "accounts/signup.html"
