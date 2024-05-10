from rest_framework import viewsets, generics, status
from vendor.models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer,UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from vendor.models import *
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone


class VendorListCreate(viewsets.ModelViewSet):
    authentication_classes = [ TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreate(viewsets.ModelViewSet):
    authentication_classes = [ TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceRetrieve(viewsets.ModelViewSet):
    authentication_classes = [ TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

class PurchaseOrderAcknowledgeViewSet(viewsets.ViewSet):
    authentication_classes = [ TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, po_id=None):
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)

        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        return Response({'message': 'Purchase order acknowledged'}, status=status.HTTP_200_OK)

class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status' : 403,'errors' : serializer.errors,'message' : 'something went wrong'})
        
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj , _ =Token.objects.get_or_create(user=user)

        return Response({'status' : 200 , 'payload' : serializer.data , 'token' : str(token_obj) , 'message' : 'your data is saved'})



