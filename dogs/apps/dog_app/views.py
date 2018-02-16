# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Dog
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    dogs=Dog.objects.all()
    context={ 'dogs': dogs}
    return render(request, 'dog_app/index.html', context)
    
def create(request):
    #print (request.POST['name'],request.POST['breed'])
    dog = Dog.objects.create(breed=request.POST['breed'],name=request.POST['name'])
    dog.save()
    return redirect('/')
    
    
def edit(request, id):
    dog=Dog.objects.get(id=id)
    context={"dog": dog}
    return render(request, 'dog_app/edit.html', context)
    
def update(request, id):
    dog=Dog.objects.get(id=id)
    dog.name=request.POST['name']
    dog.breed=request.POST['breed']
    dog.save()
    return redirect('/')
    
def delete(request, id):
    dog=Dog.objects.get(id=id)
    dog.delete()
    
    return redirect('/')