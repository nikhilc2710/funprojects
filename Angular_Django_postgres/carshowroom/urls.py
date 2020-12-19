from django.conf.urls import url
from carshowroom import views
urlpatterns=[
    url(r'^api/cars$',views.car_list),
    url(r'^aip/cars/(?P<pk>[0-9]+)$',views.cardetail),
    url(r'^api/cars/changeowner$',views.changeowner)
]