# models.py
from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import MediaCloudinaryStorage

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='portfolio/projects/',
        storage=MediaCloudinaryStorage()  # Force Cloudinary storage
    )
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    date_created = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('PROGRAMMING', 'Programming Languages'),
        ('WEB', 'Web Development'),
        ('DATABASE', 'Databases'),
        ('TOOLS', 'Tools & DevOps'),
        ('OTHER', 'Other Skills'),
    ]
    
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=50, help_text="0-100 percentage")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='PROGRAMMING'
    )
    icon_class = models.CharField(
        max_length=50,
        default='fas fa-code',
        help_text="FontAwesome icon class (e.g., 'fas fa-code')"
    )
    display_order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Higher numbers appear first"
    )
    
    class Meta:
        ordering = ['-display_order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    current = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"