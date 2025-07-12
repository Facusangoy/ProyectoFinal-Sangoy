from django.urls import path
from .views import (
    OpinionListView,
    OpinionDetailView,
    OpinionCreateView,
    OpinionUpdateView,
    OpinionDeleteView,
)

urlpatterns = [
    path('', OpinionListView.as_view(), name='opiniones'),
    path('<int:pk>/', OpinionDetailView.as_view(), name='detalle_opinion'),
    path('crear/', OpinionCreateView.as_view(), name='crear_opinion'),
    path('<int:pk>/editar/', OpinionUpdateView.as_view(), name='editar_opinion'),
    path('<int:pk>/borrar/', OpinionDeleteView.as_view(), name='borrar_opinion'),
]
