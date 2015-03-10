from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    # COMMENTED OUT url(r'^search/$', views.search, name='search'),
    url(r'^category/(?P<category_name_slug>\w+)$', views.category, name='category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^goto/$', views.track_url, name='goto'),
    url(r'^restricted/', views.restricted, name='restricted'),
    # NOT WORKING??!! url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
    # COMMENTED OUT/NOT NEEDED url(r'^register/$', views.register, name='register'),
    # COMMENTED OUT/NOT NEEDED url(r'^login/$', views.user_login, name='login'),
    # COMMENTED OUT/NOT NEEDED url(r'^logout/$', views.user_logout, name='logout'),
    )
