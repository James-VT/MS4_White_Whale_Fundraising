""" View for the blog posts """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostForm
from .models import Post

# A great deal of this code came from a number of sources:
# Fellow students Jenny, Suzy and Pmeeny, all credited in readme
# Basic code for a basic blog app came from Code With Stein (also in readme)
# and I used the other students' work to expand on that


def blog(request):
    """ Display of the blog posts """
    posts = Post.objects.all()
    template = 'blog/blog.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)


@login_required
def add_post(request):
    """ Function for adding a new blog post """

    if request.method == "POST":
        # Might need more args here?
        form = PostForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            creator = request.user
            obj.creator = creator
            obj.save()

            messages.success(request, "Your blog post was added successfully!")
            return redirect(reverse('post_detail', args=[obj.slug]))
        else:
            messages.error(
                request, "Failed to add blog post, please check for invalid \
                    form fields"
            )
    else:
        form = PostForm

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def post_detail(request, slug):
    """ Function for displaying the blog post and commenting """
    context = {}
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment_creator = request.user
            comment.comment_creator = comment_creator
            comment.save()
            messages.success(request, "Your comment was added successfully!")
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(
                request, "Comment failed, please check for invalid fields"
            )

    else:
        form = CommentForm()

    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """ View function for editing posts """
    post = Post.objects.get(slug=slug)
    user = request.user

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if user == post.creator:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                post = obj
                messages.success(request, "You have successfully edit your \
                    blog post")
                return redirect(reverse('post_detail', args=[obj.slug]))
            else:
                messages.error(request, "Failed to update blog post")
        else:
            messages.info(request, 'You need to be the post creator to do that')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)

@login_required
def delete_post(request, slug):
    """ Function for deleting a post """
    post = Post.objects.get(slug=slug)
    user = request.user
    if post.creator == user:
        post.delete()
        messages.success(request, f'Successfully deleted {post.title}')
        return redirect(reverse('blog'))

    else:
        messages.error(request, "This is not yours to delete!")

    template = 'blog/edit_post.html'
    context = {
        'post': post,
    }

    return render(request, template, context)
