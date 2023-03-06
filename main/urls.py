from django.urls import path
from .views import (
    HeaderListView, HeaderDeleteView, HeaderCreateView,
    HeaderUpdateView, HeaderView
)

urlpatterns = [
    path('', HeaderListView.as_view(), name='headers'),
    path('<int:pk>/', HeaderView.as_view(), name='header'),
    path('create/', HeaderCreateView.as_view(), name='create-header'),
    path('update/<int:pk>/', HeaderUpdateView.as_view(), name='update-header'),
    path('delete/<int:pk>/', HeaderDeleteView.as_view(), name='delete-header'),
]
