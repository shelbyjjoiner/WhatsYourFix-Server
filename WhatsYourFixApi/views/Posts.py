from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from WhatsYourFixApi.models import Posts, NeuroUser, Hobbies

class PostView(ViewSet): 

    def list(self, request): 

        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, pk, request): 

        new_post = Posts.objects.create(
            user = NeuroUser.objects.get(user=request.auth.user),
            hobbies =Hobbies.objects.get(pk=request.data["hobbies"]),
            content = request.data["content"],
            image = request.data["image"],
            item = request.data["item"]
        )

        serializer = PostSerializer(new_post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk): 

        new_post = Posts.objects.get(pk=pk)
        new_post.user = NeuroUser.objects.get(user=request.auth.user)
        new_post.hobbie = Hobbies.objects.get(pk=request.data["hobbie"])
        new_post.body = request.data["body"],
        new_post.image = request.data["image"],
        new_post.item = request.data["item"],
        new_post.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, pk): 

        post = Posts.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'user', 'content', 'image', 'item')


