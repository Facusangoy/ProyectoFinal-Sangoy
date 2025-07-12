from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Opinion

class OpinionListView(ListView):
    model = Opinion
    template_name = 'opiniones/lista.html'
    context_object_name = 'opiniones'

    def get_queryset(self):
        return Opinion.objects.order_by('-fecha')

class OpinionDetailView(DetailView):
    model = Opinion
    template_name = 'opiniones/detalle.html'

class OpinionCreateView(LoginRequiredMixin, CreateView):
    model = Opinion
    fields = ['titulo', 'contenido', 'imagen']
    template_name = 'opiniones/formulario.html'
    success_url = reverse_lazy('opiniones')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class OpinionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Opinion
    fields = ['titulo', 'contenido', 'imagen']
    template_name = 'opiniones/formulario.html'
    success_url = reverse_lazy('opiniones')

    def test_func(self):
        opinion = self.get_object()
        return self.request.user == opinion.autor

class OpinionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Opinion
    template_name = 'opiniones/confirmar_borrado.html'
    success_url = reverse_lazy('opiniones')

    def test_func(self):
        opinion = self.get_object()
        return self.request.user == opinion.autor
