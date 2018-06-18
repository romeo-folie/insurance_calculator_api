from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from calculateInsurance import views

urlpatterns= [
    # url(r'^cars/$', views.CarList.as_view(), name='car-list'),
    url(r'^cars/$', views.car_list, name='car-list'),
    # url(r'^cars/(?P<pk>[0-9]+)/$', views.CarDetail.as_view(), name='car-detail'),
    url(r'^cars/(?P<pk>[0-9]+)/$', views.car_detail, name='car-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
