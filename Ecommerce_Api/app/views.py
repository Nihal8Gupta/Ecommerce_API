from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import  status
from .serializers import *
from rest_framework.response import Response

# Create your views here.
class ProductView(APIView):
    def get(self,request):
        Pobj = Product.objects.all()
        Sobj = ProductSerializer(Pobj,many=True)
        return Response(Sobj.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        Sobj = ProductSerializer(data=request.data)
        if Sobj.is_valid():
            Sobj.save()
            return Response(Sobj.data,status=status.HTTP_201_CREATED)
        return Response(Sobj.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(APIView):
    def get(self,request,id):
        try:
            Pobj = Product.objects.get(id=id)
        except CartItem.DoesNotExist:
            msg = {'msg': 'Does Not Exist'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        Sobj = ProductSerializer(Pobj)
        return Response(Sobj.data,status=status.HTTP_200_OK)

class CartItemView(APIView): 
    def get(self,request):
        Cobj = CartItem.objects.all()
        Sobj = CartItemSerializer(Cobj,many=True)
        return Response(Sobj.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        Sobj = CartItemSerializer(data=request.data)
        if Sobj.is_valid():
            Sobj.save()
            return Response(Sobj.data,status=status.HTTP_201_CREATED)
        return Response(Sobj.errors,status=status.HTTP_400_BAD_REQUEST)

class CartItemDetail(APIView):
    def delete(self,request,id):
        try:
            Cobj = CartItem.objects.get(id=id)
        except CartItem.DoesNotExist:
            msg = {'msg': 'Does Not Exist'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        Cobj.delete()
        return Response({'message':'deleted'},status=status.HTTP_204_NO_CONTENT)

