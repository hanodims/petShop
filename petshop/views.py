from django.shortcuts import render  , redirect
from .models import Pet
from .forms import PetForm
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

def pet_create(request):
	#Complete Me
	form = PetForm()
	if request.method == "POST":
		form = PetForm(request.POST , request.FILES)
		if form.is_valid():
			form.save()
			#messages.success(request, ' add  success.')
			return redirect('pet-list')
	context = {
			"form":form,
			}
	#messages.success(request, 'create car success.')
	return render(request, 'create.html', context)


def pet_update(request, pet_id):
	#Complete Me
    pet_obj = Pet.objects.get(id=pet_id)
    form = PetForm(instance=pet_obj)
    if request.method == "POST":
    	form = PetForm(request.POST,request.FILES, instance=pet_obj)
    	if form.is_valid():
    		form.save()
    		#messages.success(request, 'Your car was updated success.')
    		return redirect('pet-detail',pet_id=pet_obj.id)
    context = {
    	"pet_obj": pet_obj,
    	"form":form,
    		}
    return render(request, 'update.html', context)


def pet_delete(request, pet_id):
	#Complete Me
	pet_obj = Pet.objects.get(id=pet_id)
	pet_obj.delete()
	#messages.success(request, ' delete  success.')
	return redirect('pet-list')
