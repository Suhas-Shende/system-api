from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import *
from django.utils import timezone
from rest_framework.authentication import BasicAuthentication
class ClientListCreateView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ClientSerializer
        return ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClientDetailSerializer
        return ClientDetailSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

class ProjectCreateView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ProjectCreateSerializer

    def post(self, request, *args, **kwargs):
        client_id = kwargs['client_id']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        project = Project.objects.create(
            project_name=serializer.validated_data['project_name'],
            client_id=client_id,
            created_by=request.user
        )
        project.users.set(serializer.validated_data['users'])
        project.save()

        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

class UserProjectsView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GetAllProjects

    def get_queryset(self):
        return self.request.user.projects.all()
