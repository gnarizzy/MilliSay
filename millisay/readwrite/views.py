from django.http import HttpResponse
from django.shortcuts import render
from readwrite.models import Post

#Displays 10 most recent posts on homepage
def index(request):
    post_list = Post.objects.order_by('-pub_date')[:10]
    context = {'posts': post_list}
    return render(request, 'readwrite/index.html',context)

