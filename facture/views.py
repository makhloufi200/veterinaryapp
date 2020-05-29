from django.shortcuts import render
from .models import Invoice, MedicationBill
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import InvoiceForm,MedicationBillForm
# Create your views here.

def list_facture(request):
	objs = Invoice.objects.all()
	
	return render(request, 'facture/list_facture.html', {'factures': objs})
	
def datail_facture(request, facture_id):
    facture = get_object_or_404(Invoice, pk=facture_id)
    return render(request, 'facture/facture.html', {'facture': facture})	
	
def create_facture(request):
    if not request.user.is_authenticated:
        raise Http404

    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('list_facture')

    return render(request, 'facture/facture_form.html', {'form': form})
	
def update_facture(request, facture_id):
	if not request.user.is_authenticated:
		raise Http404
	instance = get_object_or_404(Invoice, pk=facture_id)

	form = InvoiceForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('list_facture')

	return render(request, 'facture/facture_form.html', {"form": form,"instance": instance})


def facture_delete(request, facture_id):
    instance = get_object_or_404(Invoice, pk=facture_id)
    instance.delete()

    return redirect("list_facture")													
	
def list_facture_medecine(request):
	objs = MedicationBill.objects.all()
	
	return render(request, 'facture/list_facture _medcine.html', {'factures': objs})

	
def create_facture_medecine(request, facture_id):
	objs = MedicationBill.objects.all()
	if not request.user.is_authenticated:
		raise Http404	
	form = MedicationBillForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('list_facture_medecine')
	
	return render(request, 'facture/facture_medecine_form.html', {"form": form,"medecines": objs})	
	
def facture_medecine_delete(request, facture_id, medecine_id):
	#self.medecine.quantite = (self.medecine.quantite) + (self.quantite_medcine)
	#self.medecine.save()
	#self.facture.somme_money = (self.facture.somme_money) - (self.somme_money)
	#self.facture.save()
	instance = get_object_or_404(FactureMedecine, pk=medecine_id)
	instance.delete()
	
	return redirect("list_facture_medecine")		