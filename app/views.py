from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.conf import settings
from app.models import User_Task, File_Statuses
from app.tasks import send_on_email


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
    template_name = "app/user_task_form.html"
    fields = ('user_file',)

    def form_valid(self, form):
        user = self.request.user
        if user.is_authenticated:
            form.instance.author = user
            form.instance.file_name = form.instance.user_file.name
            self.u_email = user.email
            self.u_filename = form.instance.user_file.name
        return super().form_valid(form)

    def get_success_url(self):
        if self.u_filename:
            send_on_email.delay(self.object.user_file.url, self.u_email, self.u_filename, self.object.pk)

        return super().get_success_url()


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

    def get_success_url(self):
        if self.u_filename:
            log_file = '.' + settings.MEDIA_URL + 'file_logs/' + str(self.object.pk)
            with open(log_file, 'a', encoding='UTF-8') as f:
                f.write("файл был заменен\n")
            send_on_email.delay(self.object.user_file.url, self.u_email, self.u_filename, self.object.pk)

        return super().get_success_url()


class Delete_Task_View(DeleteView):
    model = User_Task
    success_url = "/"
