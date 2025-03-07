from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, CarPhoto
from .forms import CarForm, CarPhotoForm, RentalForm
from datetime import datetime

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    rental_price = None
    if request.method == 'POST':
        if 'photo_form' in request.POST:
            photo_form = CarPhotoForm(request.POST, request.FILES)
            if photo_form.is_valid():
                photo = photo_form.save(commit=False)
                photo.car = car
                photo.save()
                return redirect('car_detail', car_id=car.id)
        elif 'rental_form' in request.POST:
            rental_form = RentalForm(request.POST)
            if rental_form.is_valid():
                start_date = rental_form.cleaned_data['start_date']
                end_date = rental_form.cleaned_data['end_date']
                days = (end_date - start_date).days
                rental_price = days * car.price_per_day
    else:
        photo_form = CarPhotoForm()
        rental_form = RentalForm()
    return render(request, 'cars/car_detail.html', {
        'car': car,
        'photo_form': photo_form,
        'rental_form': rental_form,
        'rental_price': rental_price
    })

def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars': cars})