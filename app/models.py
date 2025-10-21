from django.db import models

# Create your models here. Models define the database schema for this app.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} — {self.email} ({self.created_at:%Y-%m-%d %H:%M})"
    
class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.state} — {self.owner}"