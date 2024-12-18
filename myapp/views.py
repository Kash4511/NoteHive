from django.shortcuts import render
from .models import varity
from django.shortcuts import get_object_or_404

# Create your views here.
def myapp(request):
    Var= varity.objects.all()
    return render(request, 'myapp/myapp.html', {'Var': Var})

def myapp_detail(request, V_ID): 
    V = get_object_or_404(varity, pk=V_ID)
    return render(request, 'myapp/myapp_detail.html', {'V': V})


