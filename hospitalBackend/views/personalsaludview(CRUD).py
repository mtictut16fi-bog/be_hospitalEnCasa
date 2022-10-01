from authApp.models.Psalud import Personal_salud
from authApp.Serializers.Psaludserializer import PersonalSaludSerializer
from rest_framework  import views, status
from rest_framework.response import Response

class crearpersonalsaludview(views.APIView):
    def post(self, request, format=None):
        serializador=PersonalSaludSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response (serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        modelo=Personal_salud.objects.all()
        serializar=PersonalSaludSerializer(modelo, many=True)
        return Response(serializar.data)

class consultarpersonalsaludview(views.APIView):
    def put(self, request, pk, format=None):
        modelo=Personal_salud.objects.get(pk=pk)
        serializacion=PersonalSaludSerializer(modelo, data=request.data)
        if serializacion.is_valid():
            serializacion.save()
            return Response (serializacion.data)
        return Response(serializacion.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modelo=Personal_salud.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk, format=None):
        modelo=Personal_salud.objects.get(pk=pk)
        serializar=PersonalSaludSerializer(modelo)
        return Response (serializar.data)