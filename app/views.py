from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.conf import settings
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.response import Response

from app.models import User_Task, File_Statuses
from app.serializers import User_Task_Serializer, List_User_Task_Serializer


class ViewData(ListView):
    model = User_Task
    success_url = '/'

    def get_queryset(self):  # переопределяем получение объектов
        super().get_queryset()
        view_data = User_Task.objects.all().filter(pk=0)
        if not self.request.user.is_anonymous:
            view_data = User_Task.objects.all().filter(author__exact=self.request.user)
        num_row = 0
        for item in view_data:
            num_row += 1
            item.num_row = num_row
            log_file = '.' + settings.MEDIA_URL + 'file_logs/' + str(item.pk)
            try:
                with open(log_file, 'r', encoding='UTF-8') as f:
                    item.rows = f.readlines()
            except:
                open(log_file, 'w', encoding='UTF-8').close()
                item.rows = []

        return view_data


class Create_Task_View(CreateView):
    model = User_Task
    success_url = "/"
    fields = ('user_file',)

    # form_class = VeiwForm

    def form_valid(self, form):
        user = self.request.user
        if user.is_authenticated:
            form.instance.author = user
            form.instance.file_name = form.instance.user_file.name
        return super().form_valid(form)


class Update_Task_View(UpdateView):
    model = User_Task
    fields = ('user_file',)
    success_url = "/"

    def form_valid(self, form):
        user = self.request.user
        if user.is_authenticated:
            form.instance.file_status = File_Statuses.RELOAD
            self.f_storage, self.f_path = self.get_object().user_file.storage, self.get_object().user_file.path
            self.f_storage.delete(self.f_path)
            form.instance.file_name = form.instance.user_file.name
            self.u_email = user.email
            self.u_filename = form.instance.user_file.name
        else:
            form.instance.author = None

        return super().form_valid(form)


class Delete_Task_View(DeleteView):
    model = User_Task
    success_url = "/"

# тут доп. задание на DRF
class List_ApiView(ListAPIView):
    queryset = User_Task.objects.all()
    serializer_class = List_User_Task_Serializer

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            view_data = super().get_queryset().filter(author__exact=self.request.user)
        else:
            raise NotAuthenticated()
        return view_data


class Detail_ApiView(RetrieveAPIView, UpdateAPIView):
    queryset = User_Task.objects.all()
    serializer_class = User_Task_Serializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise NotAuthenticated()
        obj = super().get_queryset().filter(author__exact=self.request.user, pk__exact=self.kwargs["pk"])
        if len(obj):
            return obj
        else:
            raise PermissionDenied()  # нет прав на чужие файлы

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj:
            obj.file_status = File_Statuses.RELOAD
            obj.save()
            return Response({"result": "ok", "message": "file under testing"}, status=200)
        else:
            return Response({"result": "failed", "message": "have no access to this file"}, status=403)
