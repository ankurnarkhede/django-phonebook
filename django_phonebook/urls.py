

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from phonebook import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url (r'^get-contacts/', views.contacts.as_view ()),
    url (r'^post-contacts/', views.contacts.as_view ()),


]

urlpatterns=format_suffix_patterns(urlpatterns)


