from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	status = models.TextField()
	profilePic = models.ImageField(null = True, blank = True, upload_to='profile/')
	linkvk = models.CharField(max_length=255, null=True, blank= True)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')

class Post(models.Model):
	title = models.CharField(max_length = 150)
	textPost = RichTextField(blank=True, null = True)
	imagePost = models.ImageField(blank = True, null = True, upload_to='images/')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now)
	category = models.CharField(max_length = 255, default = 'memes')
	likes = models.ManyToManyField(User, related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + '|' + str(self.author)

	def datepublished(self):
		return self.date.strftime('%d %B %Y') #d - day, B - month, Y- year

	def get_absolute_url(self):
		return reverse('article_detail', args=(str(self.id)))

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	textComment = models.TextField()
	date_added = models.DateTimeField(auto_now_add =True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)