from django.conf.urls import url
from movies import views


urlpatterns=[
url('^$', views.Home.as_view(),name="index"),
    url('^categories/$', views.AddCategory.as_view(),name="add_category"),
    url('^get-villans/$', views.ListVillans.as_view(),name="List_villans"),
    url('^villans/$', views.AddVillans.as_view(),name="add_villans"),
    url('^villans/(?P<pk>[0-9]+)/$', views.UpdateVillans.as_view(),name="update_villans"),
    url('^search/$', views.Searchview.as_view(), name="search"),
    url('^get-villans/(?P<pk>[0-9]+)/$', views.villanDetail.as_view(), name="get_villans"),

]



