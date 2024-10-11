from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .responses import CustomResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.conf import settings
from cryptography.fernet import Fernet


def encrypt_price(price):
    fernet = Fernet(settings.FERNET_KEY)
    encrypted_price = fernet.encrypt(price.encode())
    return encrypted_price

def decrypt_price(encrypted_price):
    fernet = Fernet(settings.FERNET_KEY)
    decrypted_price = fernet.decrypt(encrypted_price).decode()
    return decrypted_price


@api_view(['GET'])
def categoryList(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return CustomResponse(serializer.data, status_code=200)

@api_view(['GET'])
def categoryDetail(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return CustomResponse(serializer.data, status_code=200)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def categoryCreate(request):
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return CustomResponse(serializer.data, status_code=200)

@api_view(['PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def categoryUpdate(request, pk):
    category = Category.objects.get(id = pk)
    serializer = CategorySerializer(isinstance = category, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return CustomResponse(serializer.data, status_code=200)

@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def categoryDelete(request, pk):
    category = Category.objects.get(id = pk)
    category.delete()
    return CustomResponse("Category is deleted!!!", status_code=200)


@api_view(['GET'])
def productList(request):
    product = Product.objects.all()
    for detail in product.data:
        encrypted_price = detail.price
        detail.price = decrypt_price(encrypted_price)
    serializer = ProductSerializer(product, many=True)
    return CustomResponse(serializer.data, status_code=200)

@api_view(['GET'])
def productDetail(request, pk):
    product = Product.objects.get(id=pk)
    encrypted_price = product.data.price
    product.data.price = decrypt_price(encrypted_price)
    serializer = ProductSerializer(product, many=False)
    return CustomResponse(serializer.data, status_code= 200)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def productCreate(request):
    price = request.data.get("price")
    encrypted_price = encrypt_price(price)
    request.data.price = encrypted_price
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return CustomResponse(serializer.data, status_code= 200)

@api_view(['PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def productUpdate(request, pk):
    product = Product.objects.get(id = pk)
    serializer = ProductSerializer(isinstance =product, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return CustomResponse(serializer.data, status_code= 200)

@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def productDelete(request, pk):
    product = Product.objects.get(id = pk)
    product.delete()
    return CustomResponse("Product is deleted!!!", status_code= 200)

