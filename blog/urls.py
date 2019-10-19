from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list,name='post_list'),
    #path('',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
]
