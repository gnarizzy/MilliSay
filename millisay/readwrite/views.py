from django.http import HttpResponseRedirect
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
#Allows user to submit post, then redirects to post page if post is successful
def submit_post(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST) #create SubmitForm
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            #add new post to database, then redirect to it
    else:
        form = SubmitForm()
    return render(request, 'submit.html',{'form':form,}) #create submit.html templates




