from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Etudiant

class EtudiantListView(ListView):
    model = Etudiant
    template_name = 'etudiants/etudiant_list.html'
    context_object_name = 'etudiants'

class EtudiantDetailView(DetailView):
    model = Etudiant
    template_name = 'etudiants/etudiant_detail.html'

class EtudiantCreateView(CreateView):
    model = Etudiant
    template_name = 'etudiants/etudiant_form.html'
    fields = ['nom', 'prenom', 'date_naissance', 'email']
    success_url = reverse_lazy('etudiant-list')

class EtudiantUpdateView(UpdateView):
    model = Etudiant
    template_name = 'etudiants/etudiant_form.html'
    fields = ['nom', 'prenom', 'date_naissance', 'email']
    success_url = reverse_lazy('etudiant-list')

class EtudiantDeleteView(DeleteView):
    model = Etudiant
    template_name = 'etudiants/etudiant_confirm_delete.html'
    success_url = reverse_lazy('etudiant-list')
