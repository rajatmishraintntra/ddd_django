from django_restful_admin import admin as api,RestFulModelAdmin
from task.infrastructure.models import Task
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from task.application.validators import duplicate_validators
from django.contrib import admin


admin.site.register(Task)


@api.register(Task)
class TaskModelApi(RestFulModelAdmin):
    permission_classes=[AllowAny]
    def create(self, request, **kwargs):
        """Create new object"""
        serializer = self.get_single_serializer(data=request.data)
        if not duplicate_validators(serializer.Meta.model,name=request.data['name']):
            serializer.is_valid(raise_exception=True)
            data=serializer.data
            serializer.Meta.model.objects.create(**data)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"data":"duplicate"}, status=status.HTTP_400_BAD_REQUEST)
        

