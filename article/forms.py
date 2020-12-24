from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields =('title', 'textPost', 'author', 'category', 'imagePost')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'textPost': forms.Textarea(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
		}

class commentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'textComment')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder'}),
			'textComment': forms.TextInput(attrs={'class': 'form-control'}),
		}