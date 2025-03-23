from django.urls import path
from . import views

urlpatterns = [
    path('', views.EtudiantListView.as_view(), name='etudiant-list'),
    path('<int:pk>/', views.EtudiantDetailView.as_view(), name='etudiant-detail'),
    path('create/', views.EtudiantCreateView.as_view(), name='etudiant-create'),
    path('<int:pk>/update/', views.EtudiantUpdateView.as_view(), name='etudiant-update'),
    path('<int:pk>/delete/', views.EtudiantDeleteView.as_view(), name='etudiant-delete'),
]