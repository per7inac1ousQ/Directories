from django.conf.urls import patterns, url
from Directories import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^new$', views.create, name='create_directories'),
	url(r'^list$', views.dlist, name='list_models'),
	url(r'^edit$', views.modelUpdate, name='update_directories'),
	#url(r'^(?P<m_id>\d+)/$', views.dlist, name='list_models'),
	#url(r'^(?P<model_name>\d+)/$', views.dlist, name='list_directories'),
<<<<<<< HEAD
	#url(r'^edit/(?P<model_id>\d+)$', views.modelUpdate, name='update_directories'),
=======
	url(r'^edit/(?P<model_id>\d+)$', views.modelUpdate, name='update_directories'),
>>>>>>> afa76c68ac52b11cb70ac2e2a930c939c00d4e7f
	#url(r'^delete/(?P<pk>\d+)$', views.AttrDelete.as_view(), name='delete_directories'),
)
