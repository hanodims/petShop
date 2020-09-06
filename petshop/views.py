from django.shortcuts import render
from .models import Pet

# Create your views here.
def pet_list(request):
    context = {
        "pets": Pet.objects.all()
    }
    return render(request, 'list.html', context)


def pet_detail(request, pet_id):
    context = {
        "pet": Pet.objects.get(id=pet_id)
    }
    return render(request, 'detail.html', context)