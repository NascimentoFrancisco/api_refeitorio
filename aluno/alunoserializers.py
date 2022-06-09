from dataclasses import field
from rest_framework import serializers
from aluno.models import Aluno

class AlunoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'



