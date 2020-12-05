from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name = 'login'),
    path('profile',views.profile,name = 'profile'),
    path('logout',views.logout,name = 'logout'),
    path('edit',views.edit,name = 'edit'),
    path('update',views.update,name = 'update'),
    path('intro',views.intro,name = 'intro'),
    path('dashboard',views.dashboard,name = 'dashboard'),
    path('AdminIndex',views.AdminIndex,name = 'AdminIndex'),
    path('AdminDashboard',views.AdminDashboard,name = 'AdminDashboard'),
    path('logoutAdmin',views.logoutAdmin,name = 'logoutAdmin'),
    path('updateDashboard',views.updateDashboard,name = 'updateDashboard'),
    path('updashboard',views.updashboard,name ='updashboard'),

]
