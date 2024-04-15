from django.shortcuts import render, redirect
from .models import Contact
from ..user.models import User


def add_contact(request, user_b_id):
    current_page = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        user_a = request.user
        user_b = User.objects.get(pk=user_b_id)
        if not Contact.objects.filter(user_a=user_a, user_b=user_b).exists():
            Contact.objects.create(user_a=user_a, user_b=user_b)
    return redirect(current_page)


def remove_contact(request, user_b_id):
    current_page = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        user_a = request.user
        user_b = User.objects.get(pk=user_b_id)
        Contact.objects.filter(user_a=user_a, user_b=user_b).delete()
    return redirect(current_page)


def contacts_page(request):
    user_a = request.user
    contacts = Contact.objects.filter(user_a=user_a)
    return render(request, 'users/contacts.html', {'contacts': contacts})
