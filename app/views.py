from django.shortcuts import render

# Create your views here.
def keziya (request):
    return render(request,'venu.html')

def Gopal(request):
    return render(request,'gopal.html')

def Gopi(request):
    return render(request,'gopi.html')

def Venugopal(request):
    return render(request,'venugopal.html')