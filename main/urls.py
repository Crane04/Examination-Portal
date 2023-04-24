from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name = "index"),
    path('signin', signin, name = "signin"),
    path('signup', signup, name = "signup"),
    path('exam', exam, name = "exam"),
    path('result', result, name="result")
]