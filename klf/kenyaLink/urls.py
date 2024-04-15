from django.urls import path
from . import views


urlpatterns = [
    #main Pages
    path('' , views.home, name = 'home'),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),
    path('faqs', views.faqs, name = 'faqs'),
    

    #services
    path('permits', views.permits, name = 'permits'),
    path('passes', views.passes, name = 'passes'),
    path('visas', views.visas, name = 'visas'),
    path('permanentresidency', views.permanentresidency, name = 'permanentresidency'),
    path('citizenship', views.citizenship, name = 'citizenship'),
    #path('contact', views.contact, name = 'contact'),
    #path('contact', views.contact, name = 'contact'),
    #path('contact', views.contact, name = 'contact'),
    #path('contact', views.contact, name = 'contact'),

]

