from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('TourismPlace',viewTouristPlaces)
router.register('Hotel',viewHotel)
router.register('RateTourismPlace',viewRateTouristPlaces)
router.register('RateHotel',viewRateHotel)
router.register('FavoriteHotel',viewFavoriteHotel)
router.register('Post',viewPost)
router.register('comment',viewComment)
router.register('LikePost',viewLikePost)
router.register('HotelReservation',viewHotelReservation)

urlpatterns = [
    path('', include(router.urls)),
    path('model1/', Model1.as_view()),
]
