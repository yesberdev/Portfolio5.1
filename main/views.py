from django.shortcuts import render,  get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def cv(request):
    return render(request, 'main/cv.html')


from .models import Product
def products(request):
    products = Product.objects.all()
    context={'products': products}
    return render(request, 'main/products.html',context)

def contact(request):
    return render(request, 'main/contact.html')

# Downloading a file 
from django.http import FileResponse, Http404
import os

def download_file(request, filename):
    filepath = os.path.join('media/documents/', filename) 
    if os.path.exists(filepath):
        response = FileResponse(open(filepath, 'rb'), as_attachment=True)
        return response
    raise Http404("Файл не найден.")



from .models import BlogMessage
def blog(request):
    messages = BlogMessage.objects.all().order_by('-date')
    context = {'messages': messages}
    return render(request, 'main/blog.html', context)


def blog_detail(request, pk):
    message = get_object_or_404(BlogMessage, pk=pk)
    return render(request, 'main/blog_detail.html', {'message': message})