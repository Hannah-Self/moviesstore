from django.urls import path
#import path
from . import views
#import views

urlpatterns = [
    path('', views.index, name='home.index'),
    path('about', views.about, name='home.about'),
]
#def urlpatterns for home app
#'' = url iteself/root url, views.index = view function, name = url pattern name
