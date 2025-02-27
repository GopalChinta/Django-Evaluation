from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    points_earned = models.IntegerField(default=0)
    tasks_completed = models.IntegerField(default=0)

class App(models.Model):
    name = models.CharField(max_length=255)
    points = models.IntegerField()

    def __str__(self):
        return self.name

class Screenshot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='screenshots/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.app.name}"
