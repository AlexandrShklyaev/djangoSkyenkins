from django.urls import path

from category import views
from category.apps import CategoryConfig

app_name = CategoryConfig.name

urlpatterns = [
    path("", views.CategoryListView.as_view(), name='list'),
    path("<int:pk>/", views.CategoryDetailView.as_view(), name='detail'),
    path("create/", views.CategoryCreateView.as_view(), name='create'),
    path("edit/<int:pk>/", views.CategoryUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", views.CategoryDeleteView.as_view(), name='delete'),

    path("crib/", views.CribListView.as_view(), name='crib-list'),
    path("cat-crib/<int:pk>/", views.CatCribListView.as_view(), name='cat-crib-list'),
    path("crib/<int:pk>/", views.CribDetailView.as_view(), name='crib-detail'),
    path("crib/create/", views.CribCreateView.as_view(), name='crib-create'),
    path("crib/create/<int:pk>/", views.CatCribCreateView.as_view(), name='cat-crib-create'),
    path("crib/edit/<int:pk>/", views.CribUpdateView.as_view(), name='crib-update'),
    path("crib/delete/<int:pk>/", views.CribDeleteView.as_view(), name='crib-delete'),

]
