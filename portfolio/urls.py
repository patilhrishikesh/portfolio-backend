from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectListAPIView.as_view(), name='project-list'),
    path('skills/', views.SkillListAPIView.as_view(), name='skill-list'),
    path('about/', views.AboutMeAPIView.as_view(), name='about-me'),
]
