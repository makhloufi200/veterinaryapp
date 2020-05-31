from django.shortcuts import render
from .models import Supplier
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import PeopleForm
from django.db.models import Q
# Create your views here.

def list_people(request):
	objs = Supplier.objects.all()
	
	return render(request, 'people/list_people.html', {'peoples': objs})
	
def datail_people(request, people_id):
    people = get_object_or_404(Supplier, pk=people_id)
    return render(request, 'people/people.html', {'people': people})	
	
def create_people(request):
    if not request.user.is_authenticated:
        raise Http404

    form = PeopleForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('list_people')

    return render(request, 'people/people_form.html', {'form': form})
	
def update_people(request, people_id):
	if not request.user.is_authenticated:
		raise Http404
	instance = get_object_or_404(Supplier, pk=people_id)

	form = PeopleForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('list_people')

	return render(request, 'people/people_form.html', {"form": form,"instance": instance})


def people_delete(request, people_id):
    instance = get_object_or_404(Supplier, pk=people_id)
    instance.delete()

    return redirect("list_people")	

def search(request):
    #print (request)
    query = request.GET.get('q', '')
    
    if query:
        qset = (
        Q(name__icontains=query) |
		Q(telephone_number__icontains=query) |
		Q(email__icontains=query) |
		Q(type_people__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []

    return render(request,'home.html', {
        'books': results
    })	