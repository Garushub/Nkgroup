import os
import django
from django.core.management import call_command
from django.db.utils import IntegrityError

# Установите настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NKgroup.settings')
django.setup()

from cars.models import Car, CarPhoto

# Примеры данных для автомобилей
cars_data = [
    {
        'category': 'premium',
        'make': 'BMW',
        'model': 'X5',
        'year': 2022,
        'description': 'Отличный автомобиль для длительных поездок.',
        'price_per_day': 150.00,
        'license_plate': 'AAA111'
    },
    {
        'category': 'comfort',
        'make': 'Toyota',
        'model': 'Camry',
        'year': 2021,
        'description': 'Комфортный и надежный автомобиль.',
        'price_per_day': 100.00,
        'license_plate': 'BBB222'
    },
    {
        'category': 'economy',
        'make': 'Hyundai',
        'model': 'Elantra',
        'year': 2020,
        'description': 'Экономичный автомобиль для повседневных поездок.',
        'price_per_day': 70.00,
        'license_plate': 'CCC333'
    },
    {
        'category': 'premium',
        'make': 'Mercedes-Benz',
        'model': 'E-Class',
        'year': 2022,
        'description': 'Роскошный автомобиль с отличными характеристиками.',
        'price_per_day': 160.00,
        'license_plate': 'DDD444'
    },
    {
        'category': 'comfort',
        'make': 'Honda',
        'model': 'Accord',
        'year': 2021,
        'description': 'Комфортный автомобиль с хорошей экономией топлива.',
        'price_per_day': 110.00,
        'license_plate': 'EEE555'
    },
    {
        'category': 'economy',
        'make': 'Ford',
        'model': 'Focus',
        'year': 2019,
        'description': 'Надежный и экономичный автомобиль.',
        'price_per_day': 65.00,
        'license_plate': 'FFF666'
    },
    {
        'category': 'premium',
        'make': 'Audi',
        'model': 'A6',
        'year': 2022,
        'description': 'Элегантный и мощный автомобиль.',
        'price_per_day': 155.00,
        'license_plate': 'GGG777'
    },
    {
        'category': 'comfort',
        'make': 'Nissan',
        'model': 'Altima',
        'year': 2020,
        'description': 'Удобный автомобиль с просторным салоном.',
        'price_per_day': 105.00,
        'license_plate': 'HHH888'
    },
    {
        'category': 'economy',
        'make': 'Kia',
        'model': 'Rio',
        'year': 2018,
        'description': 'Экономичный и удобный автомобиль.',
        'price_per_day': 60.00,
        'license_plate': 'III999'
    },
    {
        'category': 'premium',
        'make': 'Lexus',
        'model': 'RX',
        'year': 2022,
        'description': 'Роскошный кроссовер с отличными характеристиками.',
        'price_per_day': 165.00,
        'license_plate': 'JJJ000'
    }
]

# Путь к папке с фотографиями
photo_path = 'NKgroup/media/car_photos'

# Добавление автомобилей и фотографий
for car_data in cars_data:
    if not Car.objects.filter(license_plate=car_data['license_plate']).exists():
        car = Car.objects.create(**car_data)
        photo_file_path = os.path.join(photo_path, f"{car.make.lower()}_{car.model.lower()}.jpg")
        if os.path.exists(photo_file_path):
            with open(photo_file_path, 'rb') as photo_file:
                CarPhoto.objects.create(car=car, photo=File(photo_file))
        print(f"Автомобиль {car.make} {car.model} успешно добавлен.")
    else:
        print(f"Автомобиль с номером {car_data['license_plate']} уже существует в базе данных.")

# Запуск миграций базы данных
call_command('migrate')

# Запуск сервера разработки
call_command('runserver', '127.0.0.1:8000')