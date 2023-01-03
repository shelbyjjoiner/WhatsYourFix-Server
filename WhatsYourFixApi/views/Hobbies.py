from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from WhatsYourFixApi.models import Hobbies, NeuroUser

class HobbieView(ViewSet):


    def list(self, request):

        hobbies = Hobbies.objects.all()
        if 'user' in request.query_params:

            user = NeuroUser.objects.get(pk=request.auth.user['user'])

            serializer = HobbieSerializer(user.hobbies, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = HobbieSerializer(hobbies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk):
        hobby = Hobbies.objects.get(pk=pk)


        serializer = HobbieSerializer(hobby, context={'request':request})
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    def create(self, request):

        new_hobbie = Hobbies.objects.create(
            label = request.data["label"]
        )
        new_hobbie.save()

        serializer = HobbieSerializer(new_hobbie, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        new_hobbie = Hobbies.objects.get(pk=pk)
        new_hobbie.label= request.data["label"]
        new_hobbie.save()

        return Response (None, status=status.HTTP_204_NO_CONTENT)



class HobbieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ('id', 'label',)