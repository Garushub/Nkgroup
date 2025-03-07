from django.db import models

class Car(models.Model):
    CATEGORY_CHOICES = [
        ('premium', 'Премиум'),
        ('comfort', 'Комфорт'),
        ('economy', 'Эконом'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    license_plate = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'

class CarPhoto(models.Model):
    car = models.ForeignKey(Car, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='car_photos/')

    def __str__(self):
        return f'Photo for {self.car.make} {self.car.model}'