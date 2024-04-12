from django.urls import path, include
from task_management_system.user.views import LoginView, RegisterView, ProfileView, logout_view, ProfileEditView, \
    about_view, UserDeleteView

urlpatterns = [
    path('about/', about_view, name='about'),

    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('<int:pk>/profile/', include([

        path('', ProfileView.as_view(), name='profile'),
        path('edit/', ProfileEditView.as_view(), name='edit profile'),
        path('delete-profile/', UserDeleteView.as_view(), name='delete profile'),

    ]))
]
