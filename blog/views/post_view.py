from django.http import HttpResponse
from django.views import generic
from blog.models import Post

from django.views import generic


class PostView(generic.ListView):
    queryset = Post.object.filter().order_by("-created_on")
    template_name = "index.html"


class PostDetail(generic.DetailView):
    model = PostView
    template_name = "post_detail.html"
