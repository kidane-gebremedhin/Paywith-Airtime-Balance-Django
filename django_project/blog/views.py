from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Post

def home(request):
	context={
		'title':'Posts',
		'posts': Post.objects.all()
	}
	#return HttpResponse('<h1>Welcome Home</h1>')
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title':'About'})

class PostListView(ListView):
	model=Post
	template_name='blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name='posts'
	ordering=['-date_posted']

class PostDetailView(DetailView):
	model=Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model=Post
	fields=['title', 'content']

	def form_valid(self, form):
			form.instance.author=self.request.user
			return super().form_valid(form)
	# def is_valid(self, form):
	# 	form.instance.author=self.request.user
	# 	return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model=Post
	fields=['title', 'content']

	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if post.author==self.request.user:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model=Post
	success_url='/'

	def test_func(self):
		post=self.get_object()
		if post.author==self.request.user:
			return True
		return False

def send_response(self, kwargs):
	data = {kwargs}
	return JsonResponse(data) 