from rest_framework import serializers
from diasletivo.models import DiaLetivo

class DiaLetivoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiaLetivo
        fields = '__all__'



