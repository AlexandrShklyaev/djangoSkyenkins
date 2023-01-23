from django.contrib import admin
from django.http import Http404
from category.models import Category, Crib


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

    def get_queryset(self, request):
        ss = 1
        if request.method == 'POST':
            if request.POST['action'] != 'delete_selected' or request.user.is_superuser:
                return super().get_queryset(request)
            else:
                return None

        return super().get_queryset(request)

@admin.register(Crib)
class CribAdmin(admin.ModelAdmin):
    list_display = ('category','name', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')