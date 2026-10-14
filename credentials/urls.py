from django.urls import path
from credentials import views

app_name="credentials"

urlpatterns=[
    path('register/',views.register,name="Sign_Up"),
    path('login/',views.login,name="Sign_In"),
    path('logout/',views.logout,name="Sign_Out"),

]