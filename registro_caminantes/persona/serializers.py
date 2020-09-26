from rest_framework import serializers
from persona.models import Caminante

class CaminanteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Caminante
        fields = ["nombre","correo","Km_semanales"]
