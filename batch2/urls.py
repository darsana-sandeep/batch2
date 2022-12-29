from django.urls import path

from batch2 import views

urlpatterns = [
    path('',views.data),
    path('create',views.create),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.Edit),
    path('edit/update/<int:id>',views.update),
    path('register',views.registration),
    path('login',views.userlogin),
    path('profile',views.profile),
    path('reg',views.UserRegister),
    path('logout',views.user_logout),
    path('teacher',views.teacherdata),
    path('index',views.indexdata),
    path('uploads',views.image_request),
    path('fkey',views.NewFunct),
    path('send',views.SendOTP),
    path('verify',views.VerifyOTP)

]