#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
from django.contrib import admin
from rec_app.api import UsersList
import rec_app.views
import rest_framework_swagger
from rec_app.views import home, auth, signout, rate_movie, movies_recs
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API name')
urlpatterns = [
    url(r'^docs/', schema_view)
]

urlpatterns += [
    url(r'^$', home, name='home'),
    url(r'^$',home, name='rec_app.views.home'),
    url(r'^auth/', auth, name='auth'),   
    url(r'^signout/',signout,name='signout'),
    url(r'^rate_movie/',rate_movie,name='rate_movie'),
    url(r'^movies-recs/',movies_recs,name='movies_recs'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users-list/',UsersList.as_view(),name='users-list'),
    url(r'^algo_loglikelihood/',rec_app.views.algo_loglikelihood,name='algo_loglikelihood'),
    url(r'^algo_userbased/',rec_app.views.algo_userbased,name='algo_userbased'),
]