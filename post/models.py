from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title =  models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.title