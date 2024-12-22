from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
               'phone_number',]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class HotelPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ['hotel_photo']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']

class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = ['room_photo']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class RoomListSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_status', 'room_type',
                  'room_price', 'room_photos']

class RoomDetailSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['room_number', 'room_status', 'room_type',
                  'room_price', 'all_inclusive', 'room_description', 'room_photos']


class HotelListSerializer(serializers.ModelSerializer):
    hotels = HotelPhotoSerializer(many=True, read_only=True)
    rooms = RoomListSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    get_count_people =serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'address', 'city', 'hotel_start', 'hotels', 'rooms', 'average_rating',
                  'get_count_people', 'reviews']

    def get_average_rating(self, obj):
        return obj.get_average_rating()



    def get_count_people(self, obj):
        return obj.get_count_people()

class CountryDetailAPIView(serializers.ModelSerializer):
    hotels = HotelListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name', 'hotels']

class HotelDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    rooms = RoomListSerializer(many=True, read_only=True)
    hotel_owner = UserProfileSimpleSerializer()
    created_date = serializers.DateField(format('%d-%m-%Y'))
    reviews = ReviewSerializer(many=True, read_only=True)
    hotel_photo = HotelPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_owner', 'hotel_description',
                  'city', 'address', 'country',
                  'rooms','hotel_start', 'hotel_video',
                  'hotel_photo', 'created_date', 'reviews']


    def get_average_rating(self, obj):
        return obj.get_average_rating()


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



