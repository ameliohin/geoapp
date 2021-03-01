
from rest_framework.response import Response
from rest_framework import generics, filters

from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.gis import geos

from django.contrib.gis.db.models.functions import Distance

from .serializers import BranchSerializer, EmployeeSerializer
from .models import Branch, Employee


class BranchesList(generics.ListAPIView):

    serializer_class = BranchSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['name',]
    filterset_fields = ['name',]

    def get_queryset(self):
        lat = self.request.query_params.get('lat', None)
        lon = self.request.query_params.get('lon', None)

        if lat and lon:
            current_point = geos.fromstr('POINT(%s %s)' % (lat, lon), srid=4326)
            queryset = Branch.objects.annotate(
                distance=Distance('location', current_point)
                ).order_by('distance')[:1]
        else:
            queryset = Branch.objects.all()

        return queryset


class EmployeesList(generics.ListAPIView):

    serializer_class = EmployeeSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['first_name', 'last_name', 'position_title', 'branch__name',]
    filterset_fields = ['branch__name',] 

    def get_queryset(self):
        return Employee.objects.all()
