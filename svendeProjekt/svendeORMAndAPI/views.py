from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.


######## Bruger
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bruger_liste(request):
    b = Bruger.objects.all()
    serializer = BrugerSerializer(b, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def bruger_create(request):
    serializer = BrugerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bruger_view(request, pk):
    b = Bruger.objects.get(id=pk)
    serializer = BrugerSerializer(b, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def bruger_update(request, pk):
    b = Bruger.objects.get(id=pk)
    serializer = BrugerSerializer(instance=b, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bruger_delete(request, pk):
    b = Bruger.objects.get(id=pk)
    b.delete()

    return Response('Bruger Deleted Successfully')
######## BrugerSlut





######## Kategori
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def kategori_liste(request):
    b = Kategori.objects.all()
    serializer = KategoriSerializer(b, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def kategori_create(request):
    serializer = KategoriSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def kategori_view(request, pk):
    b = Kategori.objects.get(id=pk)
    serializer = KategoriSerializer(b, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def kategori_update(request, pk):
    b = Kategori.objects.get(id=pk)
    serializer = KategoriSerializer(instance=b, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def kategori_delete(request, pk):
    b = Kategori.objects.get(id=pk)
    b.delete()

    return Response('Kategori Deleted Successfully')
######## KategoriSlut





######## Geo
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def geo_liste(request):
    b = Geo.objects.all()
    serializer = GeoSerializer(b, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def geo_create(request):
    serializer = GeoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def geo_view(request, pk):
    b = Geo.objects.get(id=pk)
    serializer = GeoSerializer(b, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def geo_update(request, pk):
    b = Geo.objects.get(id=pk)
    serializer = GeoSerializer(instance=b, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def geo_delete(request, pk):
    b = Geo.objects.get(id=pk)
    b.delete()

    return Response('Geo Deleted Successfully')
######## GeoSlut





######## Subscribed_kategori
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscribed_liste(request):
    b = Subscribed_kategori.objects.all()
    serializer = SubscribedKategoriSerializer(b, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribed_create(request):
    serializer = SubscribedKategoriSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscribed_view(request, pk):
    b = Subscribed_kategori.objects.get(id=pk)
    serializer = SubscribedKategoriSerializer(b, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribed_update(request, pk):
    b = Subscribed_kategori.objects.get(id=pk)
    serializer = SubscribedKategoriSerializer(instance=b, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscribed_delete(request, pk):
    b = Subscribed_kategori.objects.get(id=pk)
    b.delete()

    return Response('Subscribed kategori Deleted Successfully')
######## Subscribed_kategoriSlut





######## Billeder
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def billeder_liste(request):
    b = Billeder.objects.all()
    serializer = BillederSerializer(b, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def billeder_create(request):
    serializer = BillederSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def billeder_view(request, pk):
    b = Billeder.objects.get(id=pk)
    serializer = BillederSerializer(b, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def billeder_update(request, pk):
    b = Billeder.objects.get(id=pk)
    serializer = BillederSerializer(instance=b, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def billeder_delete(request, pk):
    b = Billeder.objects.get(id=pk)
    b.delete()

    return Response('Billeder Deleted Successfully')
######## BillederSlut