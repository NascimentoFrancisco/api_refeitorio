from rest_framework import viewsets
from refeicao.refeicaoserializers import RefeicaoSerializers
from refeicao.models import Refeicao

class RefeicaoViewsets(viewsets.ModelViewSet):
    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializers
