from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from category.forms import CategoryForm
from category.models import Category, Crib


# Create your views here.
class CategoryListView(ListView):
    model = Category
    paginate_by = 12


class CategoryDetailView(DetailView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', 'description', 'preview')
    success_url = reverse_lazy('category:list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category:list')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            super().post(request, *args, **kwargs)
        return redirect(self.success_url)


class CribListView(ListView):
    model = Crib


class CribDetailView(DetailView):
    model = Crib


class CribCreateView(CreateView):
    model = Crib
    fields = ('name', 'description', 'category')
    success_url = reverse_lazy('category:list')


class CribUpdateView(UpdateView):
    model = Crib
    fields = ('name', 'description', 'category')
    success_url = reverse_lazy('category:list')


class CribDeleteView(DeleteView):
    model = Crib
    success_url = reverse_lazy('category:list')


class CatCribCreateView(CreateView):
    model = Crib
    fields = ('name', 'description', 'category')
    success_url = reverse_lazy('category:list')

    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        if pk:
            cat = Category.objects.filter(pk=pk).first()
            self.initial.update({'category': cat})
        return super().get(request, *args, **kwargs)


class CatCribListView(ListView):
    model = Crib

    def get_queryset(self):  # переопределяем получение объектов
        pk = self.kwargs.get('pk', None)  # получаем аргумент из ссылки
        if pk is not None:  # если аргумент существует
            self.object = Category.objects.filter(pk=pk).first()
            return Crib.objects.filter(category_id__exact=pk)  # фильтруем по нему посты
        return Crib.objects.all()
