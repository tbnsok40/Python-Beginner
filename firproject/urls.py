import wordcount.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordcount.views.home, name='home'), # 이 url의 이름을 home이라 짓자, views.home 함수를 불러오는 것.
    path('about/',wordcount.views.about, name='about'),
    path('result/',wordcount.views.result, name='result'),
]
