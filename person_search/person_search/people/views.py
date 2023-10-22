from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Person
from .forms import PersonForm

def find_person(request):
    if request.method == 'POST':
        unique_id = request.POST.get('unique_id')
        try:
            person = Person.objects.get(unique_id=unique_id)
            return render(request, 'people/person_detail.html', {'person': person})
        except Person.DoesNotExist:
            raise Http404("Person does not exist")
    return render(request, 'people/find_person.html')

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('find_person')
    else:
        form = PersonForm()
    return render(request, 'people/create_person.html', {'form': form})