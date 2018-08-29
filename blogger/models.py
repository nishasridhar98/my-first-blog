from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
# to define model...models.Model means Post is a django model,so it is to be saved in the database
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)#for limited no. of char
    text = models.TextField()#long text
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

            
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #returns the post title