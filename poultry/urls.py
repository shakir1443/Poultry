from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Examples:
    # url(r'^$', 'poultry.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),

    url(r'^poultry/', include('poultryApp.urls')),
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^$', login, name='home'),
#     path('users/', include('users.urls')),
#     path('api/', include('API.urls')),
#     path('leaseholder/', include('leaseholder.urls')),
#     path('apartment/', include('apartment.urls')),
# ]
