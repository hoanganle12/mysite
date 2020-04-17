from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def xemlist(request):
    Data = {'Posts': Post.objects.all().order_by("-date")}
    return render(request, "blog/blog.html", Data)


def urlport(request, id):
    post1 = {'post': Post.objects.get(id=id)}
    return render(request, "blog/post.html", post1)


def add_post(request):
    a = PostForm()
    return render(request, "blog/add_news.html", {'f': a})


def save_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return render(request, "blog/true.html")
        else:
            return render(request, "blog/false.html")
    else:
        return render(request, "blog/false.html")


def delete(request, id):
    obj = get_object_or_404(Post, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {"object": obj}
    return render(request, "blog/delete.html", context)
