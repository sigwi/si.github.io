from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cd/',views.cd,name='cd'),
    path('cc/',views.cc,name='cc'),
    path('cb/',views.cb,name='cb'),
    path('ca/',views.ca,name='ca'),
    path('ba/',views.ba,name='ba'),
    path('ab/',views.ab,name='ab'),
    path('about/',views.about,name='about'),
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
]
