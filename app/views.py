from django.shortcuts import render

# Create your views here.
def puppy(request):
    d={'name':'puppy'}
    return render(request,'puppy.html',d)