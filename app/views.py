from django.shortcuts import render

# Create your views here.

def kona(request):
    return render(request,'general.html')
