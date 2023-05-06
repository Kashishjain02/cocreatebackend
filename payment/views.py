from django.shortcuts import render,redirect
from django.http import HttpResponse
import razorpay


def create_subscription(request):
        client = razorpay.Client(auth=("rzp_test_AvD6vsvRd1viWC", "DkkWhsoBYHSs9ubq6EbdSm9t"))

        subscription = client.subscription.create({
                'plan_id': 'plan_L8uqKh6UYnYdyf',
                'customer_notify': 1,
                'quantity': 5,
                'total_count': 6,
                # 'start_at': 1495995837,
                'addons': [{'item': {'name': 'Delivery charges', 'amount': 30000,
                        'currency': 'INR'}}],
                'notes': {'key1': 'value3', 'key2': 'value2'},
                'notify_info': {'notify_phone': 6264843056,
                        'notify_email': 'kashish.iitdelhi@gmail.com'}
                })
        print(subscription)
        print(subscription["short_url"])
        redirect(subscription["short_url"],target="_blank")
        
        return HttpResponse(subscription["short_url"])

def test(request):
        pass


def create_payment_order(request):
        client = razorpay.Client(auth=("rzp_test_AvD6vsvRd1viWC", "DkkWhsoBYHSs9ubq6EbdSm9t"))

        data = {
        "amount": 100,
        "currency": "INR",
        "receipt": "receipt#1",
        "notes": {
                "key1": "value3",
                "key2": "value2"
        }
        }
        order=client.order.create(data=data)
        print(order)

def payment_handler(request):
        return render(request,"payment/payment_handler.html")


def subscription_handler(request):
    return render(request,"payment/handler.html")
