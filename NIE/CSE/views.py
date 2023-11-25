from django.shortcuts import render

# Create your views here.
def service(request):
    return render(request,'service.html')
def contactus(request):
    return render(request,'contactus.html')
def products(request):
    return render(request,'products.html')
def aboutus(request):
    return render(request,'aboutus.html')
def home(request):
    return render(request,'home.html')