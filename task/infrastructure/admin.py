from django_restful_admin import admin as api,RestFulModelAdmin
from task.infrastructure.models import Task
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from task.application.validators import duplicate_validators,TaskDTO
from django.contrib import admin
from task.infrastructure.db_validator import UniqueValidator

admin.site.register(Task)


@api.register(Task)
class TaskModelApi(RestFulModelAdmin):
    permission_classes=[AllowAny]
    def create(self, request, **kwargs):
        """Create new object"""
        serializer = self.get_single_serializer(data=request.data)
        serializer.is_valid()
        dataw=serializer.Meta.model.objects.filter(name=request.data['name']).first()
        data=TaskDTO(name=request.data['name'],details=request.data['details'],validator={"name":UniqueValidator},obj=dataw)
        serializer.Meta.model.objects.create(**data.to_dict())
        return Response(data.to_dict(), status=status.HTTP_201_CREATED)
        

