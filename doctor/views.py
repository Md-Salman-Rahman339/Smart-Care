from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework import filters,pagination
from . import models
from . import serializers

class SpecializationViewset(viewsets.ModelViewSet):
    queryset=models.Specialization.objects.all()
    serializer_class=serializers.SpecializationSerializer


class DesignationViewset(viewsets.ModelViewSet):
    queryset=models.Designation.objects.all()
    serializer_class=serializers.DesignationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

class AvailableTImeViewset(viewsets.ModelViewSet):
    queryset=models.AvailableTIme.objects.all()
    serializer_class=serializers.AvailableTImeSerializer

class DoctorViewset(viewsets.ModelViewSet):
    queryset=models.Doctor.objects.all()
    serializer_class=serializers.DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 100


class ReviewViewset(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewSerializer
