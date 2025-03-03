from django.shortcuts import render
from .models import MyClothes

# Create your views here.
def home(request):
    return render(request, template_name='index.html')
def clothing(request):
    clothing=MyClothes.objects.all()
    context={'clothing':clothing}
    return render(request, template_name='clothing.html')
def contact(request):
    return render(request, template_name='contact.html')
def checkout(request):
    return render(request, template_name='checkout.html')