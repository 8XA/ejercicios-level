from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from persona.models import Caminante
from persona.serializers import CaminanteSerializers

@api_view(['GET','POST'])
def lista_caminantes(request):
    if request.method == 'GET':
        caminantes = Caminante.objects.all()
        serializer = CaminanteSerializers(caminantes, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CaminanteSerializers(data = request.data)
        if serializer.is_valid():
            if int(request.data["Km_semanales"]) >= 4:
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response("Debes caminar más!!!")

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
