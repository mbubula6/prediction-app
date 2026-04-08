from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('app/', views.predict_page, name='predict_page'),
    path('predict/', views.predict, name='predict'),
    path('history/', views.history, name='history'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
