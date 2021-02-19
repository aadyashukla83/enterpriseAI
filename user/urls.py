from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views as ind_views
from .forms import CustomAuthForm

urlpatterns = [
    url(r'^home$',ind_views.home,name='home'),
    url(r'^$',auth_views.login,{'template_name': 'login.html',"authentication_form":CustomAuthForm}, name='login'),
    url(r'^logout/$',auth_views.logout, {'next_page': 'users:login'}, name='logout'),
    url(r'^registration/$',ind_views.registration, name='registration'),
    url(r'^Your/Orders/$',ind_views.yourorders,name='yourorders'),
    url(r'^Confirmed/Orders/$',ind_views.confirmproducts,name='confirmedorders'),
    url(r'^chechouts/$',ind_views.chechouts,name='chechouts'),
    url(r'^view-ratings/(?P<pk>\d+)$',ind_views.viewratings,name='viewratings'),
    url(r'^Product/List/$',ind_views.productlist,name='productlist'),
    url(r'^Top/Products/$',ind_views.topproducts,name='topproducts'),
    url(r'^Graphs/$',ind_views.graphs,name='graphs'),
]