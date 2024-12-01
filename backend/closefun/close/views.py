from django.shortcuts import render
from .forms import AddressFroms

# Create your views here.




def test_home(request):
    form = AddressFroms
    return render (request , 'home.html' , {'form':form})