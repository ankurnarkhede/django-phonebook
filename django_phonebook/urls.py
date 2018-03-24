

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from phonebook import views

app_name='phonebook'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # REST url start
    url (r'^get-contacts/', views.contacts.as_view ()),
    url (r'^post-contacts/', views.contacts.as_view ()),

    # rest urls end


    # template url start
    url (r'^auth/', views.contacts.as_view ()),


    # template url end


]

urlpatterns=format_suffix_patterns(urlpatterns)


