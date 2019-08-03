from django.conf.urls import url,include
from web.views import businessunit

urlpatterns = [

    url(r'^businessunit/list/', businessunit.business_unit,name='business_unit'),
    url(r'^businessunit/add/', businessunit.business_unit_change, name='business_unit_add'),
    url(r'^businessunit/edit/(\d+)/', businessunit.business_unit_change, name='business_unit_edit'),
]
