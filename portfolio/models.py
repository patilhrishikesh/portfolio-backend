from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField()
    live_demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to = 'projects_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class AboutMe(models.Model):
    content = models.TextField()
    
    def __str__(self):
        return self.content

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TimeField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name}"