from django.shortcuts import render
from django.utils import timezone
from .models import Post #.models implies0 current directory
# Create your views here.
#A view is a place where we put the "logic" of our application. It will request information from the model you created before and pass it to a template
#to connect model nd templates
from django.shortcuts import render
from django.utils import timezone



def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blogger/post_list.html', {'posts':posts})


