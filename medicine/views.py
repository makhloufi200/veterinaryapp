from django.shortcuts import render
from .models import Medicine
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import MedicineForm
# Create your views here.

def list_medecine(request):
	objs = Medicine.objects.all()
	
	return render(request, 'medecine/list_medecine.html', {'medecines': objs})
	
def datail_medecine(request, medicine_id):
    medecine = get_object_or_404(Medicine, pk=medicine_id)
    return render(request, 'medecine/medecine.html', {'medecine': medecine})	
	
def create_medecine(request):
    if not request.user.is_authenticated:
        raise Http404

    form = MedicineForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('list_medecine')

    return render(request, 'medecine/medecine_form.html', {'form': form})
	
def update_medecine(request, medicine_id):
	if not request.user.is_authenticated:
		raise Http404
	instance = get_object_or_404(Medicine, pk=medicine_id)

	form = MedicineForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('list_medecine')

	return render(request, 'medecine/medecine_form.html', {"form": form,"instance": instance})


def medecine_delete(request, medicine_id):
    instance = get_object_or_404(Medicine, pk=medicine_id)
    instance.delete()

    return redirect("list_medecine")													