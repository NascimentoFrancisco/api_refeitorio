from rest_framework import viewsets
from diasletivo.diasletivoserializers import DiaLetivoSerializers
from diasletivo.models import DiaLetivo

class DiaLetivoViewsets(viewsets.ModelViewSet):
    queryset = DiaLetivo.objects.all()
    serializer_class = DiaLetivoSerializers
