from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .views import login_view
app_name='core'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('items/', include('item.urls')),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    #path('login/', views.custom_login_view, name='login')
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    path('items/', views.items_view, name='items'),
    # path('categories/', views.categories, name='categories'),
    #path('test/', views.test_view, name='test')
    #path('login/', views.asview(template_ame='core/login.html'), name='login')
    # this ensure that URL pattern for the login view exists and has the name 'login'
] 