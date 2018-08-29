from django.contrib import admin

# Register your models here.
from blogger.models import Post

admin.site.register(Post) 
# To make our model visible on the admin page, we need to register the model 
