from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.db.utils import IntegrityError
from django.urls import reverse

from account.models import Account,Startup,Mentor
from mentorconnect.models import Meeting,TempMeeting
from rest_framework.decorators import api_view, permission_classes

from rest_framework.authtoken.models import Token
import razorpay

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
#             print(data[ 0])
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
    token = request.headers.get('Authorization')
    user = Token.objects.get(key=token).user
    print(user.id)
    if request.method == "POST":
        date = request.data.get('date')
        time = request.data.get('time')
        print(date,time)
        if user.is_startup:
            # user=Account.objects.get(email=user.email)
            meet=TempMeeting.objects.get(startup=user.id)
            meet.date=date
            meet.time=time
            meet.save()
        return Response({'msg': 'data recieved'})




 
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
# @permission_classes([IsAuthenticated])
@permission_classes([])
def create_payment_order(request):
    if request.method == "POST":
        amount = request.data.get('amount')
        client = razorpay.Client(auth=("rzp_test_AvD6vsvRd1viWC", "DkkWhsoBYHSs9ubq6EbdSm9t"))
        amount=int(amount)
        data = {
        "amount": int(amount),
        "currency": "INR",
        "receipt": "receipt#1",
        "notes": {
                "key1": "value3",
                "key2": "value2"
        }
        }
        order=client.order.create(data=data)
        print(order)
        return Response(order)

def payment_handler(request):
        return render(request,"payment/payment_handler.html")


@api_view(['POST'])
def payment_success(request):
    print("##success##")
    token = request.headers.get('Authorization')
    user = Token.objects.get(key=token).user
    if request.method == 'POST':
        amount = request.data.get('amount')
        # payment_id = request.POST.get('razorpay_payment_id')
        # order_id = request.POST.get('razorpay_order_id')
        # signature = request.POST.get('razorpay_signature')
        user.credits+=int(amount)
        user.save()
        return Response({'msg': 'data recieved'})
        
        # return render(request,"payment/payment_success.html")
