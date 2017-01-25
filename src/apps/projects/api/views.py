from rest_framework import viewsets

from apps.projects.api.serializers import ProjectSerializer
from apps.projects.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for ``Project`` model"""

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
