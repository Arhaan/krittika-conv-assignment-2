from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .forms import PostCreateForm, UserCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib import messages



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


def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("posts-list")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserCreateForm()
    return render(request=request, template_name="registration/register.html", context={"form":form})
