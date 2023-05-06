from django.shortcuts import render
from account.models import Startup,Mentor
from django.http import HttpResponseRedirect, HttpResponse
from .serializers import StartupSerializer,MentorSerializer,AccountSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.db.utils import IntegrityError
from django.urls import reverse

from account.models import Account
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout, login, authenticate

# @csrf_exempt
# @api_view(['GET',])
# # @permission_classes([IsAuthenticated])
# @permission_classes([])
# def product_api(request, id=None):
#     if request.method == "GET":
#         if id is None:
#             data = Product.objects.all()
#             serializer = ProductSerializer(data, many=True)
#             # print("hellloooo",serializer.data[0])
#             for i in serializer.data:
#                 sub = SubCategory2.objects.get(id=i['subcategory2'])
#                 i['subcategory2'] = sub.name
#                 i['subcategory1'] = sub.subcategory1.name
#                 i['category'] = sub.subcategory1.category.name
#
#             return Response(serializer.data)
#
#         else:
#             # data = Product.objects.get(pk=id)
#             data = Product.objects.filter(pk=id)
#             serializer = ProductSerializer(data, many=True)
#             print(data[0])
#             serializer.data[0]['subcategory2'] = data[0].subcategory2.name
#             serializer.data[0]['subcategory1'] = data[0].subcategory2.subcategory1.name
#             serializer.data[0]['category'] = data[0].subcategory2.subcategory1.category.name
#             # print(serializer.data)
#             return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         # print(serializer.data)
#         if serializer.is_valid():
#             data = serializer.data
#             vendor = VendorAccount.objects.get(email=request.user.email)
#             data["vendor"]=vendor
#             data.save()
#
#             # serializer.save()
#             return Response({'msg', 'DATA CREATED'})
#         return Response(serializer.errors)
#
#     if request.method == 'PUT':
#         data = Product.objects.get(pk=id)
#         serializer = ProductSerializer(data, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             print("PUT data", serializer.data)
#             return Response({'msg', 'Data Updated'})
#         return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         data = Product.objects.get(pk=id)
#         data.delete()
#         return Response({'msg': 'data deleted'})


@csrf_exempt
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
@permission_classes([])
def test_api(request, id=None):
    if request.method == "POST":
        mentor = request.data.get('mentor')
    pass




 
@csrf_exempt
@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
@permission_classes([])
def creditinfo(request):
    token = request.headers.get('Authorization')
    user = Token.objects.get(key=token).user
    # do something with the user object
    if request.method == 'GET':
        data=[{"credits":user.credits}]
        return Response(data)

    if request.method == "POST":
        mentor = request.data.get('mentor')
        price = request.data.get('price')
        if user.credits>=price:
            user.credits-= price
            user.save()
            

        else:
            return Response({'error': 'Insufficient Funds'})

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(email=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        print("login successful")
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'})

@csrf_exempt
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
@permission_classes([])
def startupdata(request, id=None):
    if request.method == 'GET':
        data = Startup.objects.all()
        serializer = StartupSerializer(data, many=True)    

        return Response(serializer.data)

@api_view(['POST'])
def user_registration(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # user = serializer.validated_data['id']
        user=Account.objects.get(email=serializer.validated_data['email'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': 'User registration successful'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def startup_registration(request):
    print("data########",request.data)
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')
    contact_number = request.data.get('phone')
    startup_name=request.data.get('companyName')
    
    user = Account.objects.create_user(
                name=name, email=email, password=password, contact_number=contact_number, viewpass=password
            )
    user.is_startup = True
    user.save()

    startup = Startup.objects.create(
                startup_name=startup_name, founder=user,phone=contact_number
            )
    startup.save()
    
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@csrf_exempt
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
@permission_classes([])
def mentor(request, id=None):
    print(id)
    if request.method == 'GET':
        if id==None:
            data = Mentor.objects.all()
            print(data)
            serializer = MentorSerializer(data, many=True)    
            print(serializer.data)
            return Response(serializer.data)
        else:
            data = Mentor.objects.filter(pk=id)
            serializer = MentorSerializer(data, many=True)
    
            print(serializer.data)
            return Response(serializer.data)


# Url:
#		1) list: https://<your-domain>/api/list
#		2) pagination: http://<your-domain>/api/list?page=2
#		3) search: http://<your-domain>/api/list?search=mitch
#		4) ordering: http://<your-domain>/api/list?ordering=-date_updated
#		4) search + pagination + ordering: <your-domain>/api/list?search=shirt&page=2&ordering=-date_updated
# http://127.0.0.1:8000/api/list/?brand=elpizo
# Headers: Authorization: Token <token>

# @permission_classes((AllowAny, ))
# class ApiProductListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated,)
#     pagination_class = PageNumberPagination
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     filterset_fields = ['brand', 'size']
#     search_fields = ('name', 'subcategory2__name', 'desc')