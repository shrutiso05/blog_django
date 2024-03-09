from django.shortcuts import render , redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_deatil', pk=pk)
        else:
            form = CommentForm()
        return render(request, 'blog/post_detail.html',{'post':post, 'comments' : comments, 'form' : form})
# Create your views here.