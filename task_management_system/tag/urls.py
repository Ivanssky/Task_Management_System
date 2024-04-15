from django.urls import path, include
from .views import tag_list, delete_tag

urlpatterns = [

    path('tags/', tag_list, name='tag list'),
    path('tags/<int:tag_id>/delete/', delete_tag, name='delete tag'),

]
