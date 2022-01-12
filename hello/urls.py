from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Techstar Mahesh Admin"
admin.site.site_title = "Techstar Mahesh Admin Portal"
admin.site.index_title = "Welcome to Techstar Mahesh Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
