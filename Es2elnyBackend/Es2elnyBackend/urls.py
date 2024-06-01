from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('questions/', include('questions.urls')),  # Make sure to add a trailing slash
    path('serliny/admins/', admin.site.urls),
]