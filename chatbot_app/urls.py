from django.urls import path
from chatbot_app import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about.html', views.about, name="about"),
    path('process_input/', views.process_input, name='process_input'),
]
