from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from readwrite.models import Post

#Displays 10 most recent posts on homepage
def index(request):
    post_list = Post.objects.order_by('-pub_date')[:10]
    context = {'posts': post_list}
    return render(request, 'readwrite/index.html',context)
#Displays the requested post, or a 404 page
def post_detail(request, postid):
    post = get_object_or_404(Post, pk=postid)
    return render(request, 'readwrite/post.html',{'post':post})


