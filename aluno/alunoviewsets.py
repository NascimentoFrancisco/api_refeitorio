from rest_framework import viewsets
from aluno.alunoserializers import AlunoSerializers
from aluno.models import Aluno

class AlunoViewsets(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializers
