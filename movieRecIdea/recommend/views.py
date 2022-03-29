from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'recommend/home.html')


def faq(request):
    return render(request, 'recommend/faq.html')
