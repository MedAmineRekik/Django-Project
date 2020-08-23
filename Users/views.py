from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import User
from .forms import ProductForm

class UserList(ListView):
    model = User

class UserDetail(DetailView):
    model = User

class UserCreate(SuccessMessageMixin, CreateView):
    model = User
    form_class = ProductForm
    success_url = reverse_lazy('user_list')
    success_message = "User successfully created!"

class UserUpdate(SuccessMessageMixin, UpdateView):
    model = User
    form_class = ProductForm
    success_url = reverse_lazy('user_list')
    success_message = "User successfully updated!"

class UserDelete(SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('user_list')
    success_message = "User successfully deleted!"


