from django.conf.urls import patterns, url
from Directories import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^new$', views.create, name='create_directories'),
	url(r'^list$', views.dlist, name='list_models'),
	#url(r'^(?P<m_id>\d+)/$', views.dlist, name='list_models'),
	#url(r'^(?P<model_name>\d+)/$', views.dlist, name='list_directories'),
	#url(r'^(?P<model_name>\d+)/$', dlistView.as_view()),
	#url(r'^edit/(?P<pk>\d+)$', views.AttrUpdate.as_view(), name='update_directories'),
	#url(r'^delete/(?P<pk>\d+)$', views.AttrDelete.as_view(), name='delete_directories'),
)
