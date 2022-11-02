from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer, UserSerializer

from .models import Post
from django.contrib.auth.models import User

# Create your views here.

@api_view(["GET"])
def home(request, *args, **kwargs):
    posts = Post.objects.all()
    seriliazer = PostSerializer(posts, many=True)
    return Response(seriliazer.data, status=200)


@api_view(["GET"])
def auth_user(request, *args, **kwargs):
    posts = User.objects.all()
    seriliazer = UserSerializer(posts, many=True)
    return Response(seriliazer.data, status=200)


@api_view(["POST"])
def create_post(request, *args, **kwargs):

    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(creator=request.user)

        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

# def home(request, *args, **kwargs):
#     posts = Post.objects.all()
#     context = [
#         {
#             "id": post.id,
#             "title": post.title,
#             "content": post.content,
#             "image": post.url_path,
#             "creator": post.creator.username if post.creator else None,
#             "date_created": post.created
#         } for post in posts
#     ]
#     return JsonResponse(context, safe=False)



# def create_post(request, *args, **kwargs):
#     title = request.POST.get("title")
#     content = request.POST.get("content")

#     print(title)
#     print(content)

#     post = Post.objects.create(
#         title=title, 
#         content=content, 
#         creator=request.user
#         )

#     context = {
#         {
#             "id": post.id,
#             "title": post.title,
#             "content": post.content,
#             "image": post.url_path,
#             "creator": post.creator.username if post.creator else None,
#             "date_created": post.created
#         } 
#     }

#     return JsonResponse(context)

    
