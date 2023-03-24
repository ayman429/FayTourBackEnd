from allauth.account.views import confirm_email
# <<<<<<< HEAD
# from django.conf.urls import url
from django.urls import re_path as url
# from django.urls import re_path
# =======
from django.urls import re_path as url

# >>>>>>> 51f3c73ff9037e98cccb284f22fb1efced265469
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]