from . import views
from django.urls import  path

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
     path('resetPassword/', views.resetPassword, name='resetPassword'),
]
