from django.shortcuts import render, redirect
from .models import BrandData
from .forms import BrandDataFrom
import requests

# Create your views here.


def index(request):
    data = BrandData.objects.all()

    # response = requests.get('https://shop.kz/noutbuki/')
    # data2 = response.json()
    # print(data2)

    if request.method == 'POST':
        form = BrandDataFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BrandDataFrom()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)
