from pets.models import Pet
from pets.serializers import PetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#List all Pet, or create a new pet.
class PetList(APIView):
    def get(self, request, format=None):
        pet = Pet.objects.all()
        serializer = PetSerializer(pet, many=True)
        return Response(serializer.data)

class AddPet(APIView):
    def post(self, request, format=None):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Retrieve, update or delete a snippet instance.
class PetViewDetails(APIView):
    def get_object(self,pk):
        try:
            return self.Pet.objects.get(pk = pk)
        except self.Pet.objects.get(pk = pk).DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        pet = self.get_object(pk)
        serializer = PetSerializer(pet)
        return Response(serializer.data)

    def put(self, request, pk,format = None):
        pet = self.get_object(pk)
        serializer = PetSerializer(pet,data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pet = self.get_object(pk)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


