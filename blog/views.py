from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .forms import PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin



from .models import Post
from django.urls import reverse
# Create your views here.

class PostDetailsView(DetailView):
    model = Post
    template_name = "blog/detailblog.html"

class PostListView(ListView):
    model = Post
    template_name = "blog/listblogs.html"

class PostCreateView(LoginRequiredMixin ,FormView):
    template_name = "blog/createblog.html"
    form_class = PostCreateForm
    success_url = "/view_blog/" # TODO: Do this using reverse

    def form_valid(self, form):
        p = Post.objects.create(author=self.request.user, title=self.request.POST['title'], content=self.request.POST['content'])
        p.save()
        return super().form_valid(form)
