from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from WhatsYourFixApi.models import Comments, NeuroUser, Posts

class CommentView(ViewSet): 

    def list(self, request): 

        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def create(self, request):

        user = NeuroUser.objects.get(user=request.auth.user)
        post = Posts.objects.get(pk=request.data["post"])
        comment = Comments.objects.create(
            user = user, 
            post = post,
            body = request.data["body"],
            
        )

        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def destroy(self, request, pk): 
        comment = Comments.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CommentSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Comments
        fields = ('id', 'user', 'post', 'body')