from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoursListView.as_view(), name='cours-list'),
    path('<int:pk>/', views.CoursDetailView.as_view(), name='cours-detail'),
    path('create/', views.CoursCreateView.as_view(), name='cours-create'),
    path('<int:pk>/update/', views.CoursUpdateView.as_view(), name='cours-update'),
    path('<int:pk>/delete/', views.CoursDeleteView.as_view(), name='cours-delete'),
]