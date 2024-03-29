from User.serializers import UserSerializer
from rest_framework import serializers
from .models import *


class TourismImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismImages
        fields = ['image']

class HotelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelsImages
        fields = ['image']

class TouristPlacesSerializer(serializers.ModelSerializer):
    images = TourismImagesSerializer(many=True,read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length=1000000,allow_empty_file=False,use_url=False),
        write_only=True
    )

    rate_one_by_one = serializers.SerializerMethodField('rate_one_by_one_func')
    created_by = serializers.SerializerMethodField('touristPlaces_created_by')
    class Meta:
        model = TouristPlaces
        fields = ['id','name','type','address','description','coordinatesX','coordinatesY','originalImage',
                  'uploaded_images','images','no_of_ratings','avg_ratings','rate_one_by_one','user','created_by']# 'video',

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        touristPlaces = TouristPlaces.objects.create(**validated_data)

        for image in uploaded_images:
            new_image = TourismImages.objects.create(touristPlaces=touristPlaces, image=image)
        return touristPlaces

    def rate_one_by_one_func(request,self):
        ratings = RateTouristPlaces.objects.filter(touristPlaces=self)
        length = len(ratings)
        star1 = RateTouristPlaces.objects.filter(touristPlaces=self,stars=1).count()
        star2 = RateTouristPlaces.objects.filter(touristPlaces=self,stars=2).count()
        star3 = RateTouristPlaces.objects.filter(touristPlaces=self,stars=3).count()
        star4 = RateTouristPlaces.objects.filter(touristPlaces=self,stars=4).count()
        star5 = RateTouristPlaces.objects.filter(touristPlaces=self,stars=5).count()
        if length !=0:
            list_of_rate = {"1":int((star1/length)*100),"2":int((star2/length)*100),"3":int((star3/length)*100),
                            "4":int((star4/length)*100),"5":int((star5/length)*100)}

        else: list_of_rate = {"1":0,"2":0,"3":0,"4":0,"5":0}

        return list_of_rate

    def touristPlaces_created_by(request,self):
        json = {
            "id":self.user.id,
            "userName":self.user.username,
            "email":self.user.email
            }
        print(json)
        return json


class HotelSerializer(serializers.ModelSerializer):
    images = HotelImagesSerializer(many=True,read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length=1000000,allow_empty_file=False,use_url=False),
        write_only=True
    )

    rate_one_by_one = serializers.SerializerMethodField('rate_one_by_one_func')
    created_by = serializers.SerializerMethodField('hotel_created_by')

    class Meta:
        model = Hotel
        fields = ['id','name','description','coordinatesX','coordinatesY','address','City','Phone','web','email',
                  'Single','Double','Triple','Sweet','chalet','villa','totalRooms','TotalBeds',
                  'no_of_ratings','avg_ratings','rate_one_by_one','images','originalImage','uploaded_images','user','created_by'
                ]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        hotel = Hotel.objects.create(**validated_data)

        for image in uploaded_images:
            newproduct_image = HotelsImages.objects.create(hotel=hotel, image=image).image
        return hotel

    def rate_one_by_one_func(request,self):
        ratings = RateHotel.objects.filter(hotel=self)
        length = len(ratings)
        star1 = RateHotel.objects.filter(hotel=self,stars=1).count()
        star2 = RateHotel.objects.filter(hotel=self,stars=2).count()
        star3 = RateHotel.objects.filter(hotel=self,stars=3).count()
        star4 = RateHotel.objects.filter(hotel=self,stars=4).count()
        star5 = RateHotel.objects.filter(hotel=self,stars=5).count()
        if length !=0:
            list_of_rate = {"1":int((star1/length)*100),"2":int((star2/length)*100),"3":int((star3/length)*100),
                            "4":int((star4/length)*100),"5":int((star5/length)*100)}

        else: list_of_rate = {"1":0,"2":0,"3":0,"4":0,"5":0}
        return list_of_rate

    def hotel_created_by(request,self):
        json = {
            "id":self.user.id,
            "userName":self.user.username,
            "email":self.user.email
            }
        return json


class RateTouristPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateTouristPlaces
        fields = '__all__'

class RateHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateHotel
        fields = '__all__'



# --------------------------------------------------------
class FavoriteTouristPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteTouristPlaces
        fields = ['id','user','touristPlaces','fav']
# --------------------------------------------------------
class FavoriteHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteHotel
        fields = ['id','user','hotel','fav']


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ['image']

class PostSerializer(serializers.ModelSerializer):
    images = PostImagesSerializer(many=True,read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length=1000000,allow_empty_file=False), 
        write_only=True,
        required=False
    )
    comment_numbers = serializers.SerializerMethodField('number_of_comments_func')
    like_numbers = serializers.SerializerMethodField('number_of_likes_func')
    created_by = serializers.SerializerMethodField('post_created_by')
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Post
        fields = ['id','user','body','uploaded_images','images','created_by','created_at','updated_at','comment_numbers','like_numbers']


    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images",[])
        post = Post.objects.create(**validated_data)

        for image in uploaded_images:
            new_image = PostImages.objects.create(post=post, image=image)
        return post

    def number_of_comments_func(request,self):
        Commentnumbers = Comment.objects.filter(post=self).count()
        return str(Commentnumbers)

    def number_of_likes_func(request,self):
        Likenumbers = LikePost.objects.filter(post=self).count()
        return str(Likenumbers)

    def post_created_by(request,self):
        json = {
            "id":self.user.id,
            "userName":self.user.username,
            "email":self.user.email,
            "image":self.user.image.url if self.user.image else ""
            }
        print(json)
        return json


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = ['id','user','post','like']

class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField('comment_created_by')
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Comment
        fields = ['id','user','post','comment','created_by','created_at','updated_at','current_time']

    def comment_created_by(request,self):
        json = {
            "id":self.user.id,
            "userName":self.user.username,
            "email":self.user.email,
            "image":self.user.image.url if self.user.image else ""
            }
        print(json)
        return json

class HotelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelReservation
        fields = ['id','user','hotel','phone_number','adulls','kids','check_in','check_out','created_at','updated_at']




