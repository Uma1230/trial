from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post

# Create your views here.
class PostList(ListView):
	queryset = Post.objects.order_by('-date')
	template_name = 'blog/blog.html'

def postdetail(request, id):
	post = Post.objects.get(id=id)
	return render(request,'blog/posttemplate.html', {'post' : post})