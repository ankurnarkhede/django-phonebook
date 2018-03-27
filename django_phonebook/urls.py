

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from phonebook import views

app_name='phonebook'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # REST url start
    url (r'^api-contacts/', views.api_contacts.as_view (), name='api_contacts'),

    # rest urls end


    # template url start
    url (r'^auth/$', views.LoginView.as_view (), name='login_user'),
    url (r'^signup/$', views.UserFormView.as_view (), name='signup_user'),
    url (r'^logout/$', views.LogoutView.as_view (), name='logout_user'),
    url (r'^$', views.Home.as_view (), name='index'),
    # url (r'^/(?P<msg>\w+)$', views.Home.as_view (), name='index'),
    url (r'^contacts/', views.contacts.as_view (), name='contacts' ),
    url (r'^contacts-view/', views.contacts_home.as_view (), name='contacts-view' ),


# url (r'^project/(?P<project_id>\d+)/$','user_profile.views.EditProject', name='edit_project'),,


    # template url end


]

urlpatterns=format_suffix_patterns(urlpatterns)


