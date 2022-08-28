from django.urls import path
from polls import views

urlpatterns = [
    path('get_gender/', views.get_gender),
]