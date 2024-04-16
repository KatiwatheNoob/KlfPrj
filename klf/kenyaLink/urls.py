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
    path('permanent-residency', views.permanentResidency, name = 'permanent-residency'),
    path('citizenship', views.citizenship, name = 'citizenship'),

    #permits
    path('class-c', views.classC, name = 'class-c'),
    path('class-d', views.classD, name = 'class-d'),
    path('class-g', views.classG, name = 'class-g'),
    path('class-i', views.classI, name = 'class-i'),
    path('class-k', views.classK, name = 'class-k'),
    path('class-m', views.classM, name = 'class-m'),

    #passes

    path('dependant-pass', views.dependantPass, name = 'dependant-pass'),
    path('extension-pass', views.extensionPass, name = 'extension-pass'),
    path('student-pass', views.studentPass, name = 'student-pass'),
    path('special-pass', views.specialPass, name = 'special-pass'),
    path('re-entry-pass', views.reEntryPass, name = 're-entry-pass'),

    #permanent residency
    path('category-a', views.categoryA, name = 'category-a'),
    path('category-b', views.categoryB, name = 'category-b'),
    path('category-c ', views.categoryC, name = 'category-c'),
    path('category-d', views.categoryD, name = 'category-d'),


]

