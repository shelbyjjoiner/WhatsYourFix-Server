from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from WhatsYourFixApi.models import NeuroUser, Posts, Hobbies
from rest_framework.decorators import action


class NeuroUserView(ViewSet):

    def list(self, request):
        user = User.objects.get(pk=request.auth.user_id)
        log_user = NeuroUser.objects.get(user=request.auth.user)
        users = NeuroUser.objects.all().exclude(user_id=log_user.user_id)


        serializer = NeuroUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk=None):
        user = NeuroUser.objects.get(pk=pk)

        serializer = NeuroUserSerializer(user, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user = NeuroUser.objects.get(pk=pk)
        user.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=True)
    def profile(self, request, pk):

        user = NeuroUser.objects.get(user=request.auth.user)

        serializer =NeuroUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class NeuroUserHobbieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ('id', 'label',)

class NeuroUserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'hobbies', 'body', 'image', 'item',)

class NeuroUserSerializer(serializers.ModelSerializer):
    posts = NeuroUserPostSerializer(many =True)
    hobbies = NeuroUserHobbieSerializer(many =True)
    class Meta:
        model = NeuroUser
        fields = ('id', 'full_name', 'bio', 'posts', 'hobbies',)

