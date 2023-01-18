from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sede
from .serializers import SedeSerializer
from core.permissions import isAdminOrEncargadoOrSuperUser

class SedeListAPI(APIView):
  permission_classes = [isAdminOrEncargadoOrSuperUser]
  def get(self,request,format=None):
    sedes=Sede.objects.order_by('-timestamps')[0:5]
    serializer=SedeSerializer(sedes,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

  def post(self,request,format=None):
    serializer=SedeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SedeQueryAPI(APIView):
  permission_classes = [isAdminOrEncargadoOrSuperUser]
  def get(self,request,kword,format=None):
    sedes=Sede.objects.filter(sede__icontains=kword)
    serializer=SedeSerializer(sedes,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

class SedeDetailAPI(APIView):
  permission_classes=[isAdminOrEncargadoOrSuperUser]  
  def get(self,request,pk):
    try:
      sede=Sede.objects.get(pk=pk)
      serializer=SedeSerializer(sede)
      return Response(serializer.data,status=status.HTTP_200_OK)
    except Sede.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  
  def post(self,request,pk):
    try:
      sede=Sede.objects.get(pk=pk)
      serializer=SedeSerializer(sede,data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Sede.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  def delete(self,request,pk):
    try:
      sede=Sede.objects.get(pk=pk)
      sede.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    except Sede.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)