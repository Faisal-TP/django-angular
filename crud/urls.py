
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^user/$',views.addfn),
   url(r'^user/([0-9]+)$',views.addfn)
]
