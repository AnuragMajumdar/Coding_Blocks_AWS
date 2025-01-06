from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, logout_view, UserDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', UserDetailView.as_view(), name='user_details'),
]

