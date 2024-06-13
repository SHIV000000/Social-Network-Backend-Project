from rest_framework import viewsets
from .models import Discussion, Hashtag, Comment
from .serializers import DiscussionSerializer, HashtagSerializer, CommentSerializer
from django.shortcuts import render
from django.http import JsonResponse
from .models import Discussion
from users.models import User



class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

    def get_queryset(self):
        queryset = Discussion.objects.all()
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            queryset = queryset.filter(hashtags__name__icontains=tag)
        text = self.request.query_params.get('text', None)
        if text is not None:
            queryset = queryset.filter(text__icontains=text)
        return queryset

class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# API to create a post
def create_post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        image = request.FILES.get('image')
        tags = request.POST.get('tags').split(',')

        discussion = Discussion.objects.create(text=text, image=image, tags=tags)
        discussion.save()
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

# API to load discussions
def load_discussions(request):
    discussions = Discussion.objects.all()
    discussions_list = [{'text': d.text, 'image': d.image.url if d.image else None, 'tags': d.tags} for d in discussions]
    return JsonResponse({'discussions': discussions_list})

# API to search users
def search_users(request):
    name = request.GET.get('name')
    users = User.objects.filter(name__icontains=name)
    users_list = [{'name': u.name, 'email': u.email} for u in users]
    return JsonResponse({'users': users_list})
