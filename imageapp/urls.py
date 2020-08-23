from django.urls import path, include

from .views import ItemListView,ItemDetailView,ItemCreateView,ItemEditView


urlpatterns = [
    path('items/',ItemListView.as_view()),
    path('items/<int:pk>/',ItemDetailView.as_view()),
    path('items/add',ItemCreateView.as_view()),
    path('items/<int:pk>/edit',ItemEditView.as_view()),
]
