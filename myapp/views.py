from django.shortcuts import render
from .models import varity

# Create your views here.
def myapp(request):
    Var= varity.objects.all()
    return render(request, 'myapp/myapp.html', {'Var': Var})

