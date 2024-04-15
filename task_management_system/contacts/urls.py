from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts_page, name='contacts'),
    path('add_contact/<int:user_b_id>/', views.add_contact, name='add_contact'),
    path('remove_contact/<int:user_b_id>/', views.remove_contact, name='remove_contact'),
]
