from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('select_course/', views.select_course, name='select_course'),
    path('add_user/', views.add_user, name='add_user'),
    path('login1/', views.login1, name = 'login1'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('signup/', views.signup, name='signup')
]

