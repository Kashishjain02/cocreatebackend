from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from .models import Account, Startup
# from django.contrib.auth.models import auth, User
from django.contrib.auth import logout, login, authenticate
from account.forms import AccountAuthenticationForm
import requests
import json

#for redirecting to a url by name
from django.urls import reverse

#for generating unique code
import uuid


from datetime import date
# from django.core.files.storage import default_storage
# from twilio.rest import Client
# from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse



# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


def uniquecode():
    # this function returns a unique code everytime it is called
    return uuid.uuid4().hex


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

def userregister(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact_number = request.POST['phone']
        email = request.POST['email']
        password = request.POST.get('password')

        try:
            Account.objects.get(email=email)
            msg = email + " is already registered,if you think there is a issue please contact us at 6264843506"
            return HttpResponse(msg)
        except Account.DoesNotExist:
            user = Account.objects.create_user(
                name=name, email=email, password=password, contact_number=contact_number, viewpass=password
            )
            user.save()
            login(request, user)
            msg = "User Registration Successful"
            return HttpResponse(msg)
    else:
        return render(request, "account/register.html")

# @login_required(login_url="../login")
# features to be added
# 1. if user clicks on become a vendor then send a message to admin
# 2. a vendor who has cancelled subscription comes back
def create_store(request):
    user=request.user
    if user.is_authenticated:
        if user.is_vendor==True:
            return HttpResponse("User already has a store")

        if request.method == 'POST':
            phone = request.POST['phone']
            state = request.POST['state']
            city = request.POST['city']
            shop_name = request.POST['name']
            gst = request.POST['gst']
            address = request.POST['address']

            store = Store.objects.create(
                shop_name=shop_name, phone=phone, address=address, city=city,
                state=state, vendor=user,email=user.email,gst=gst
                )
            store.save()
            user.is_vendor=True
            
            return HttpResponse("store successfuly created")
        return render(request,"account/user_to_vendor.html")
    
    else:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST.get('password')
            phone = request.POST['phone']
            state = request.POST['state']
            city = request.POST['city']
            shop_name = request.POST['shopname']
            gst = request.POST['gst']
            address = request.POST['address']
            user = Account.objects.create_user(
                name=name, email=email, password=password, contact_number=phone, viewpass=password
            )
            user.save()
            store = Store.objects.create(
                shop_name=shop_name, phone=phone, address=address, city=city,
                state=state, vendor=user,email=user.email,gst=gst
                )
            store.save()
            user.is_vendor=True
            user.save()
            return HttpResponse("store successfuly created")
        return render(request,"account/vendor_registration.html")
        

    

# def create_store(request):


    if request.method == 'POST':
        name = request.POST['name']
        shop_number = request.POST.get('phone')
        email = request.POST['email']
        password = request.POST.get('password')
        try:
            main_user = Account.objects.create_user(
                name=name, email=email, password=password, contact_number=shop_number, viewpass=password
            )
            main_user.save()
            msg = "User Registration Successful"

        except Exception as e:
            msg = e
            return render(request, "account/vendorregister.html", {'msg': msg})

        shop_number = request.POST.get('shop_number')
        shopname = request.POST.get('shopname').lower()
        shop_add_flat = request.POST['shop_add_flat']
        shop_add_city = request.POST['shop_add_city']
        shop_add_state = request.POST['shop_add_state']
        vendor = Account.objects.get(email=email)
        vendor.is_Vendor = True
        vendor.save()
        plan = request.POST.get('plan')

        try:
            user = VendorAccount.objects.create(
                shop_name=shopname, shop_number=shop_number, shop_add=shop_add_flat, city=shop_add_city,
                state=shop_add_state, plan=plan, vendor=vendor,
                subscripton_amount=subscription_amount, email=email)
            user.save()

        except IntegrityError as e:
            e = str(e)
            if e == "UNIQUE constraint failed: account_vendoraccount.shop_name":
                shopname = shopname + uniquecode()

                user = VendorAccount.objects.create(
                    shop_name=shopname, shop_number=shop_number, shop_add=shop_add, plan=plan, vendor=vendor,
                    subscripton_amount=subscription_amount, email=email)
                user.save()
            else:
                msg = "vendor already registered,if you think there is a issue please contact us at 6264843506"
                return render(request, "account/vendorregister.html", {'msg': msg})

        # twilio message
        # account_sid = 'AC58aae686ada0a42728e123cfee24cd5b'
        # auth_token = '1d2bfa8c3b98e92dd3d9c271fba9463e'
        # client = Client(account_sid, auth_token)
        #
        # message = client.messages \
        #     .create(
        #     body="a new vendor has registored, email=" + email + "shopname =" + shopname + "and contact_number is " + str(
        #         mobile),
        #     from_='+14159696324',
        #     to='+916264843506'
        # )

        # print(message.sid)

        # return redirect("../subscription")
        msg = "Vendor Registration Successful"
        login(request, main_user)
        return render(request, 'payment/payu/payu_payment.html', {'amount': subscription_amount})
        return render(request, 'shop/dashboard.html', {'vendor': vendor})
    else:
        return render(request, "account/user_to_vendor.html")

def userlogin(request):
    msg = ""
    user = request.user
    if user.is_authenticated:
        # return redirect("../")
        return redirect(reverse('index'))
    else:
        if request.POST:
            email = request.POST['email']
            password = request.POST['password']
            print(email, password,request.POST)
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                request.user = user
                next = request.POST.get('next', '../')
                if next == "":
                    next=reverse('index')
                return redirect(next)
                # return redirect('../')
            else:
                msg = "invalid Email or password"
    
    return render(request, 'account/login.html', { "msg": msg})



@login_required(login_url="../login")
def logoutuser(request):
    logout(request)
    return redirect("../")




@login_required(login_url="../login")
def changepassword(request):
    global msg
    password = request.POST.get('password')
    new_password = request.POST.get('new_password')
    confirm_password = request.POST.get('confirm_password')
    user = authenticate(email=request.user.email, password=password)
    if user:
        if new_password == confirm_password:
            userid = request.user.id
            u = Account.objects.get(id=userid)
            u.set_password(new_password)
            u.save()
            Account.objects.filter(id=userid).update(viewpass=new_password, )
            msg = "Password Changed"
        else:
            msg = "new password does not match with confirm password"
    else:
        msg = "Wrong password"
    return redirect("../account")


    custId = "order" + str(request.user.id)

    global plan
    global promocode
    global code

    value = 00
    if plan == "starter":
        value = 20
    elif plan == "economic":
        value = 50
    elif plan == "advanced":
        value = 200
    if value == 00:
        value = 50
    # value=10
    for i in code:
        if promocode == i:
            value = code[i]

    value = str(value)
    paytmParams = dict()

    paytmParams["body"] = {
        "requestType": "NATIVE_SUBSCRIPTION",
        "mid": "vgADHx05412495283112",
        "websiteName": "WEBSTAGING",
        "orderId": custId,
        "callbackUrl": "http://127.0.0.1:8000/handlesubscription/",
        "subscriptionAmountType": "FIX",
        "subscriptionStartDate": str(date.today()),
        "autoRenewal": True,
        "subscriptionGraceDays": "1",
        "subscriptionFrequency": "1",
        "subscriptionFrequencyUnit": "MONTH",
        "subscriptionExpiryDate": "2031-05-20",
        "subscriptionEnableRetry": "1",
        "txnAmount": {
            "value": value,
            "currency": "INR",
        },
        "userInfo": {
            "custId": custId,
        },
    }

    checksum = Checksum2.generateSignature(json.dumps(paytmParams["body"]), MERCHANT_KEY)
    print("checksum: :", checksum)
    paytmParams["head"] = {
        "signature": checksum
    }
    post_data = json.dumps(paytmParams)

    # for Staging
    url = "https://securegw-stage.paytm.in/subscription/create?mid=vgADHx05412495283112&orderId= " + \
          paytmParams["body"]["orderId"]

    # for Production
    # url = "https://securegw.paytm.in/subscription/create?mid=vgADHx05412495283112&orderId=ORDERID_98765"

    response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()
    print(response)
    global subsId
    subsId = response["body"]["subscriptionId"]
    return render(request, 'account/paytm.html', {'response': response, 'orderId': paytmParams["body"]["orderId"]})


