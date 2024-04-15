from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm, ProfileForm, ProfileEditForm
from .models import User
from ..contacts.models import Contact


def main_page(request):
    return render(request, 'home.html')


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid email or password")
            return self.form_invalid(form)


class RegisterView(CreateView):
    template_name = 'users/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ProfileView(DetailView):
    model = User
    form_class = ProfileForm
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_user = self.request.user
        users_profile_pk = self.kwargs.get('pk')
        in_contacts = False
        current_profile = User.objects.get(pk=users_profile_pk)
        if current_user.pk != current_profile.pk:

            if Contact.objects.filter(user_a=current_user, user_b=current_profile).exists():
                in_contacts = True


        context['current_user'] = current_user
        context['current_profile'] = current_profile
        context['in_contacts'] = in_contacts
        return context


class ProfileEditView(UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = 'users/edit_profile.html'
    success_url = 'profile'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


def logout_view(request):
    logout(request)
    return redirect("home")


def about_view(request):
    return render(request, 'about.html')


def user_search(request):
    search_query = request.GET.get('q')
    users = User.objects.none()
    if search_query:
        users = User.objects.filter(username__icontains=search_query)
    return render(request, 'search_results.html', {'users': users, 'query': search_query})


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'users/delete_profile.html'

    def test_func(self):
        return self.request.user.is_staff or self.request.user.pk == self.kwargs.get('pk')




