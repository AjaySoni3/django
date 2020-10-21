from django.urls import path
from appfive import views

# template urls

app_name = 'appfive'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
]