from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from readwrite.models import Post
from readwrite.forms import PostForm

#Displays 20 most recent top posts on homepage. Change to index once everything works
def index(request):
    post_list = Post.objects.filter(is_top=True).order_by('-pk')[:20]
    context = {'posts': post_list}
    return render(request, 'readwrite/index.html', context)

#Displays 20 most recent posts on homepage
def new(request):
    post_list = Post.objects.order_by('-pk')[:20]
    context = {'posts': post_list}
    return render(request, 'readwrite/new.html', context)

#Displays the requested post, or a 404 page
def post_detail(request, postid):
    post = get_object_or_404(Post, pk=postid)
    previous = 1
    next = 1
    try: #fetch previous post to link on requested post page, or go to about page
        previous = post.get_previous_by_pub_date().id
    except:
        pass
    try: #fetch next post to link on request post page, or go to about page
        next = post.get_next_by_pub_date().id
    except:
        pass
    context = {'post': post,'previous':previous,'next':next}
    return render(request, 'readwrite/post.html',context)

#Allows user to submit post, then redirects to post page if post is successful
def submit_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            post = Post.objects.order_by('-pk')[0]
            length = len(post.content.split())
            Post.objects.filter(pk=post.pk).update(words=length)
            url = '/post/' + str(post.pk)
            return HttpResponseRedirect(url)
        #Do word count on front end
    else:
        form = PostForm()
    return render(request, 'readwrite/submit.html',{'form':form,})




