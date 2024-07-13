from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('', views.home, name='home'),
    path('about/', views.About, name='about'),
    path('prediction/', views.prediction, name='prediction'),
    path('contact/', views.Contact, name='contact'),
    path('logout/', views.logout_user, name='logout'),
]
