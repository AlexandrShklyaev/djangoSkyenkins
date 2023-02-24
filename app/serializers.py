from rest_framework import serializers

from app.models import User_Task


class List_User_Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = User_Task
        fields = ("id", "file_name", "modified", "file_status")

class User_Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model  = User_Task
        fields = "__all__"


