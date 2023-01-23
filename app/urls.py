from django.urls import path

from app import views

urlpatterns = [
    path("", views.ViewData.as_view(), name='User_Task_list'),
    path("create_task/", views.Create_Task_View.as_view(), name='create_task'),
    path("update_task/<int:pk>/", views.Update_Task_View.as_view(), name='update_task'),
    path("delete_task/<int:pk>/", views.Delete_Task_View.as_view(), name='delete_task'),

]
