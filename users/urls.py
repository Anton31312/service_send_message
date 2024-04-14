from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users import views

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/genpassword', views.generate_new_password, name='generate_new_password'),
    path('verify/', views.activate_user),
    path('user_list/', views.get_users_list, name='list_view'),
    path('activity/<int:pk>/', views.toogle_activity, name='toogle_activity'),

]