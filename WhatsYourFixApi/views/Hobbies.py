from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from WhatsYourFixApi.models import Hobbies 

class HobbieView(ViewSet):

    def retrieve(self, request, pk=None):
        hobby = Hobbies.objects.get()

        serializer = HobbieSerializer(hobby,  context={'request':request})
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):

        hobbies = Hobbies.objects.all()
        serializer = HobbieSerializer(hobbies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request): 

        new_hobbie = Hobbies.objects.create(
            label = request.data["label"]
        )
        new_hobbie.save()
        
        serializer = HobbieSerializer(new_hobbie, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, pk):
        hobby = Hobbies.objects.get(pk=pk)
        hobby.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class HobbieSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Hobbies
        fields = ('id', 'label',)