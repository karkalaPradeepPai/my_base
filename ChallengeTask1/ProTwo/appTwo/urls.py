from django.urls import include, path
from appTwo import views

urlpatterns = [
    path('',views.help,name='help'),
]
