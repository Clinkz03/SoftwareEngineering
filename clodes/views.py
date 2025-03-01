from django.shortcuts import render
from .models import MyClothes

# Create your views here.
def home(response):
    return render(response, template_name='index.html')
def clothing(request):
    clothing=MyClothes.objects.all()
    context={'clothing':clothing}
    return render(request, template_name='clothing.html')
def contact(response):
    return render(response, template_name='contact.html')
def checkout(response):
    return render(response, template_name='checkout.html')