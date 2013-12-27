from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from readwrite.models import Post
from readwrite.forms import PostForm
import re

#Displays 10 most recent posts on homepage
def index(request):
    post_list = Post.objects.order_by('-pub_date')[:30]
    context = {'posts': post_list}
    return render(request, 'readwrite/index.html', context)
#Displays the requested post, or a 404 page
def post_detail(request, postid):
    post = get_object_or_404(Post, pk=postid)
    return render(request, 'readwrite/post.html',{'post':post})
#Allows user to submit post, then redirects to post page if post is successful
def submit_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            count = Post.objects.count()
            post = get_object_or_404(Post, pk=count)
            length = len(re.findall(r'\w+', post.content))
            Post.objects.filter(pk=count).update(words=length)
            url = '/post/' + str(count)
            return HttpResponseRedirect(url)
        #Do word count on front end
    else:
        form = PostForm()
    return render(request, 'readwrite/submit.html',{'form':form,}) #create submit.html template




