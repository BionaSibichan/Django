from django.urls import path
from credentials import views

urlpatterns=[
    path('register/',views.register,name="Sign_Up"),
    path('login/',views.login,name="Sign_In")
]