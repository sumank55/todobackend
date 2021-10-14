from django.shortcuts import render
from .models import Plan
from .serializers import PlanSerializers
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
# Create your views here.


class PlanList(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers

class PlanCreate(CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers


class PlanDestroye(DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers
    lookup_field = 'id'



