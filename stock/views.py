from django.shortcuts import render
from .models import BuyMedicine
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import StockForm
from people.models import Supplier
# Create your views here.

def list_stock(request):
	objs = BuyMedicine.objects.all()
	
	return render(request, 'stock/list_stock.html', {'stocks': objs})
	
def datail_stock(request, stock_id):
    stock = get_object_or_404(BuyMedicine, pk=stock_id)
    return render(request, 'stock/stock.html', {'stock': stock})	
	
def create_stock(request):
	if not request.user.is_authenticated:
		raise Http404

	form = StockForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('list_stock')

	return render(request, 'stock/stock_form.html', {'form': form})
	
def update_stock(request, stock_id):
	if not request.user.is_authenticated:
		raise Http404
	instance = get_object_or_404(BuyMedicine, pk=stock_id)

	form = StockForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('list_stock')

	return render(request, 'stock/stock_form.html', {"form": form,"instance": instance})


def stock_delete(request, stock_id):
    instance = get_object_or_404(BuyMedicine, pk=stock_id)
    instance.delete()

    return redirect("list_stock")													