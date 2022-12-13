from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from WhatsYourFixApi.models import Hobbies 

class HobbieView(ViewSet):

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

class HobbieSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Hobbies
        fields = ('id', 'label',)