from django.urls import path
from .views import HomeView, ArticleDetailView, addPostView, editPostView, deletePostView, addCategoryView, CategoryView, CategoryListView,LikeView, addCommentView

urlpatterns = [
	path('', HomeView.as_view(), name = "home"),
	path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
	path('create/', addPostView.as_view(), name='addPost'),
	path('addcategory/', addCategoryView.as_view(), name='addCategory'),
	path('edit/<int:pk>', editPostView.as_view(), name='editPost'),
	path('article/<int:pk>/remove', deletePostView.as_view(), name='deletePost'),
	path('category/<str:namecat>', CategoryView, name='category'),
	path('category-list/', CategoryListView, name='category_list'),
	path('like/<int:pk>', LikeView, name='like_post'),
	path('article/<int:pk>/comment/', addCommentView.as_view(), name='add_comment'),
]