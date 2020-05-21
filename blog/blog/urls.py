
from django.contrib import admin
from django.urls import path

from blogapp.views import firsthome, detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', firsthome, name='firsthome'),
    path('blog2/<int:blog_id>/', detail, name='detail'),
]
