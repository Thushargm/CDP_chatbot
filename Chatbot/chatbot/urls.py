from django.urls import path
from chatbot.views import get_response
from . import views

urlpatterns = [
     path('', views.chatbot_home, name='chatbot_home'),
     path('get_response/', get_response, name='get_response'),
     path('test-openai/', views.openai_test, name='openai_test'),
]
