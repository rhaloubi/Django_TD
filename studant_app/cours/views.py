from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cours

class CoursListView(ListView):
    model = Cours
    template_name = 'cours/cours_list.html'
    context_object_name = 'cours'

class CoursDetailView(DetailView):
    model = Cours
    template_name = 'cours/cours_detail.html'

class CoursCreateView(CreateView):
    model = Cours
    template_name = 'cours/cours_form.html'
    fields = ['titre', 'description', 'code_cours']
    success_url = reverse_lazy('cours-list')

class CoursUpdateView(UpdateView):
    model = Cours
    template_name = 'cours/cours_form.html'
    fields = ['titre', 'description', 'code_cours']
    success_url = reverse_lazy('cours-list')

class CoursDeleteView(DeleteView):
    model = Cours
    template_name = 'cours/cours_confirm_delete.html'
    success_url = reverse_lazy('cours-list')
