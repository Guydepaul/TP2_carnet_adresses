from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.liste_contacts, name='liste_contacts'),
    path('ajout/', views.ajout_contact, name='ajout_contact'),
    path('<int:contact_id>/', views.details_contact, name='details_contact'),
]
