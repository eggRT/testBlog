from django.urls import path
from .views import UserRegisterView, UserUpdateView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView

urlpatterns = [
 		path('register/', UserRegisterView.as_view(), name='register'),
		path('edit_profile/', UserUpdateView.as_view(), name='changeprofile'),
 		path('<int:pk>/profile', ShowProfilePageView.as_view(), name='profile_page'),
 		path('profile/edit/<int:pk>', EditProfilePageView.as_view(), name='edit_profile_page'),
 		path('create_profile/', CreateProfilePageView.as_view(), name='createprofile'),
 ]