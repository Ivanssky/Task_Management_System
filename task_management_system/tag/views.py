from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag
from .forms import TagForm


def tag_list(request):
    tags = Tag.objects.filter(name__in=['Home', 'Work', 'Other'])
    return render(request, 'tag/tag_list.html', {'tags': tags})



def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    tag.delete()
    return redirect('tag_list')
