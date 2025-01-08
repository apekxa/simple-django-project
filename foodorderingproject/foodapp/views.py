from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse,HttpResponseRedirect
from .import models

# Create your views here.

from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

class HomeView(TemplateView):
    template_name = 'foodapp/home.html'

class MenuView(TemplateView):
    template_name = 'foodapp/menu.html'

class GalleryListView(TemplateView):
    template_name = 'foodapp/gallery_food.html'

class FoodTimingView(TemplateView):
    template_name = 'foodapp/food_timing.html'

class FoodContactView(TemplateView):
    template_name = 'foodapp/food_contact.html'