from rest_framework.views import APIView
from rest_framework.response import Response

from posts import models
from .serializers import PostSerializer


class PublicPostList(APIView):
    """
        Return most recent public posts for all users
    """

    def get(self, request, *args, **kwargs):
        posts = models.Post.objects.public_posts()[:5]
        data = PostSerializer(posts, many=True)
        return Response(data.data)