from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} by {self.author.email}"
    