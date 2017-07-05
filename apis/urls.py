from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apis import views
version = 'v1'

urlpatterns = [

    url(r'^location/(?P<pk>[0-9]+)$', views.location_detail),
    url(r'^location/$', views.location_list),

    url(r'^department/(?P<pk>[0-9]+)$', views.department_detail),
    url(r'^department/$', views.department_list),

    url(r'^category/(?P<pk>[0-9]+)$', views.category_detail),
    url(r'^category/$', views.category_list),

    url(r'^subcategory/(?P<pk>[0-9]+)$', views.subcategory_detail),
    url(r'^subcategory/$', views.subcategory_list),

    url(r'^flatdata/(?P<pk>[0-9]+)$', views.flatdata_detail),
    url(r'^flatdata/$', views.flatdata_list),

    url(r'^importdata/$', views.import_data),

    url(r'^api/'+version+'/location/(?P<pk>[0-9]+)/department/$', views.location_rel),
    url(r'^api/'+version+'/department/(?P<pk>[0-9]+)/category/$', views.department_rel),
    url(r'^api/'+version+'/category/(?P<pk>[0-9]+)/subcategory/$', views.category_rel),
    url(r'^api/'+version+'/subcategory/(?P<pk>[0-9]+)/product/$', views.subcategory_rel),

]

urlpatterns = format_suffix_patterns(urlpatterns)
