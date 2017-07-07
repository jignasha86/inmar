from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apis import views
version = 'v1'
base_url = 'api/'+version

urlpatterns = [

    url(r'^'+base_url+'/location/(?P<pk>[0-9]+)$', views.location_detail),
    url(r'^'+base_url+'/location$', views.location_list),

    url(r'^'+base_url+'/department/(?P<pk>[0-9]+)$', views.department_detail),
    url(r'^'+base_url+'/department$', views.department_list),

    url(r'^'+base_url+'/category/(?P<pk>[0-9]+)$', views.category_detail),
    url(r'^'+base_url+'/category$', views.category_list),

    url(r'^'+base_url+'/subcategory/(?P<pk>[0-9]+)$', views.subcategory_detail),
    url(r'^'+base_url+'/subcategory$', views.subcategory_list),

    url(r'^'+base_url+'/flatdata/(?P<pk>[0-9]+)$', views.flatdata_detail),
    url(r'^'+base_url+'/flatdata$', views.flatdata_list),

    url(r'^'+base_url+'/importdata$', views.import_data),

    url(r'^'+base_url+'/flare$', views.flare_data),

    url(r'^'+base_url+'/location/(?P<pk>[0-9]+)/department$', views.location_rel),
    url(r'^'+base_url+'/department/(?P<pk>[0-9]+)/category$', views.department_rel),
    url(r'^'+base_url+'/category/(?P<pk>[0-9]+)/subcategory$', views.category_rel),
    url(r'^'+base_url+'/subcategory/(?P<pk>[0-9]+)/product$', views.subcategory_rel),

]

urlpatterns = format_suffix_patterns(urlpatterns)
