from django.shortcuts import render, get_object_or_404, reverse 
from django.views import generic, View
from django.http import HttpResponseRedirect 
from .models import Post
from profiles.models import UserProfile


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html" 


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/blog_detail.html",
            {
                "post": post,
                "liked": liked,
            },
        )
   
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/blog_detail.html",
            {
                "post": post,
                "liked": liked
            },
        )


class PostLike(View):
   
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        profile = UserProfile.objects.get(user=request.user)
        print('USER: ', request.user)
        print('USER Profile: ', profile)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(profile)
        else:
            post.likes.add(profile)


        return HttpResponseRedirect(reverse('post_detail', args=[slug])) 
