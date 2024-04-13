from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
# from users.views import RegisterView, ProfileView, activate_user, generate_new_password, get_users_list, toogle_activity

app_name = UsersConfig.name

urlpatterns = [
    # path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    # path('profile/genpassword', generate_new_password, name='generate_new_password'),
    # path('verify/', activate_user),
    # path('user_list/', get_users_list, name='list_view'),
    # path('activity/<int:pk>/', toogle_activity, name='toogle_activity'),

]