from django.contrib import admin
from django.urls import path, include

from task_management_system.task.views import HomeView
from task_management_system.user import views
from django.conf import settings
from django.conf.urls.static import static

from task_management_system.user.views import user_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('user/search/', user_search, name='user search'),
    path('', include('task_management_system.contacts.urls')),
    path('', include('task_management_system.priority.urls')),
    path('', include('task_management_system.tag.urls')),
    path('', include('task_management_system.task.urls')),
    path('', include('task_management_system.user.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
