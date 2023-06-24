from django.shortcuts import render, redirect

from FruitApp.web.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, ProfileEditForm
from FruitApp.web.models import Fruit, Profile


# Create your views here.

def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }
    return render(request, 'common/dashboard.html', context)


def fruit_create(request):
    form = FruitCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form
    }
    return render(request, 'fruits/create-fruit.html', context)


def fruit_details(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    context = {
        'fruit': fruit
    }
    return render(request, 'fruits/details-fruit.html', context)


def fruit_edit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    form = FruitEditForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'fruits/edit-fruit.html', context)


def fruit_delete(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    form = FruitDeleteForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'fruits/delete-fruit.html', context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    fruit = Fruit.objects.all()
    number_of_post = len(fruit)

    context = {
        'number_of_post': number_of_post
    }
    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    if request.method == 'POST':
        Profile.objects.first().delete()
        Fruit.objects.all().delete()
        return redirect('index')

    return render(request, 'profile/delete-profile.html')
