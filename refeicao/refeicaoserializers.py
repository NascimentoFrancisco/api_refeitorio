from rest_framework import serializers
from refeicao.models import Refeicao

class RefeicaoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Refeicao
        fields = '__all__'

