from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('simpleUser', 'simpleUser'),
        ('ownerUser', 'ownerUser'),
    )
    status = models.CharField(max_length=16, choices=ROLE_CHOICES, default='simpleUser')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[ MinValueValidator(18),
                                                        MaxValueValidator(70)],
                                                        null=True, blank=True)


class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.country_name



class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    hotel_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_description = models.TextField()
    city =models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='hotels')
    hotel_start = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                               MaxValueValidator(5)])
    hotel_video = models.FileField(upload_to='hotel_video/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
      return f'{self.hotel_name}  - {self.city}'


    def get_average_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


    def get_count_people(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return ratings.count()
        return 0


class HotelPhoto(models.Model):
    hotel  = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotels')
    hotel_photo = models.ImageField(upload_to='hotel_photos/', null=True, blank=True)


class Room(models.Model):
    room_number = models.PositiveSmallIntegerField()
    hotel_room = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    TYPE_CHOICES = (
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('одноместный', 'одноместный'),
        ('двухместный', 'двухместный')

    )
    room_type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    STATUS_CHOICES = (
        ('свободен', 'свободен'),
        ('забронрован', 'забронрован'),
        ('занят', 'занят')
    )
    room_status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='свободен')
    room_price = models.PositiveIntegerField()
    all_inclusive = models.BooleanField(default=False)
    room_description = models.TextField()


    def __str__(self):
        return f'{self.hotel_room} - {self.room_type} - {self.room_number}'

class RoomPhoto(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_photos')
    room_photo = models.ImageField(upload_to='room_photos')

class Review(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_review = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(null=True, blank=True)
    stars =models.IntegerField(max_length=16, choices=[(i, str(i)) for i in range(1, 6)])
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.user_name} - {self.hotel_review} - {self.stars}'


    class Meta:
      unique_together = ('user_name', 'hotel_review',)

class Booking(models.Model):
    hotel_book = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_book = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_book = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_BOOK_CHOICES = (
        ('отменено', 'отменено'),
        ('подтверждено', 'подтверждено')
    )

    status_book = models.CharField(max_length=16, choices=STATUS_BOOK_CHOICES)

    def __str__(self):
        return f'{self.hotel_book} - {self.room_book} - {self.user_book} - {self.status_book}'



