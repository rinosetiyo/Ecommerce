from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def product_detail(request):
    return render(request, 'pages/product-detail.html')