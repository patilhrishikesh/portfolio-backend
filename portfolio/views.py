from django.shortcuts import render
from rest_framework import generics
from .serializers import ProjectSerializer, SkillSerializer, AboutMeSerializer
from .models import Project, Skill, AboutMe
# Create your views here.

class SkillListAPIView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class AboutMeAPIView(generics.RetrieveAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    
    def get_object(self):
        return AboutMe.objects.first()