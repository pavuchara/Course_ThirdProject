from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person
from .forms import PersonForm


def index(request):
    form = PersonForm()
    people = Person.objects.all()
    context = {
        'form': form,
        'people': people,
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')


def edit(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
        if request.method == 'POST':
            form = PersonForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/')
        else:
            form = PersonForm(instance=person)
            return render(request, 'edit.html', {'form': form})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')


def delete(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')
