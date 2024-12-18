from django.urls import path
from . import views

# localhost:8000/myapp
urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('<int:V_ID>/', views.myapp_detail, name='detail'),
    path('myapp/<int:id>/', views.myapp_detail, name='myapp'),
]
