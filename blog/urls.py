from django.urls import path, include

from blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('<slug:slug>/', views.PostView.as_view(), name='post_detail'),
]
