from rest_framework import viewsets
from rest_framework import permissions
from .models import Member
from .serializes import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    