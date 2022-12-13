from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from WhatsYourFixApi.models import NeuroUser 


class NeuroUserView(ViewSet):
    
    def list(self, request):
        users = NeuroUser.objects.all()

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


class NeuroUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = NeuroUser
        fields = ('id', 'full_name', 'bio',)