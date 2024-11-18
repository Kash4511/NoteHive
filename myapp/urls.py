
from django.urls import path
from . import views

# localhost:8000/myapp
urlpatterns = [
    path('', views.myapp, name='myapp'),  

]
