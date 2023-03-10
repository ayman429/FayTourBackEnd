"""project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
# from rest_framework.authtoken.views import TokenObtainPairView,
# from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User.urls')),
    path('api/', include('FayTourApp.urls')),

    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 

    # path('rest-auth', include('rest_framework.urls')),
    # path('rest-auth/token/', TokenObtainPairView.as_view()),
    # path('rest-auth/token/refresh/', TokenRefreshView.as_view()),
]