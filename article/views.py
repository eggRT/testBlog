from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, commentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	namecat = Category.objects.all()
	ordering = ['-date']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked= True

	return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})

def CategoryView(request, namecat):
	category_posts = Post.objects.filter(category =namecat.replace('-', ''))
	return render(request, 'categories.html', {'namecat': namecat.replace('-',' ').title(), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_detail.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes=stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["total_likes"] = total_likes
		context["cat_menu"] = cat_menu
		context["liked"] = liked
		return context

class addCommentView(CreateView):
	model = Comment
	template_name = 'add_comment.html'
	form_class = commentForm
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

class addPostView(CreateView):
	model = Post
	template_name = 'add_post.html'
	form_class = PostForm
	success_url = reverse_lazy('home')
	#fields = ('title', 'textPost', 'author')

class addCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'

class editPostView(UpdateView):
	model = Post
	template_name = 'edit_post.html'
	form_class = PostForm
	success_url = reverse_lazy('home')

class deletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')