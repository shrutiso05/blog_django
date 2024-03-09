from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title =  models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete= models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publicatation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    