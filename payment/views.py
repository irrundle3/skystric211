from django.shortcuts import render, get_object_or_404
from main.models import Order
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.conf import settings
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')

@csrf_exempt
def payment_cancelled(request):
    return render(request, 'payment/cancelled.html')

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.totalprice,
            'item_name': 'Order {}'.format(order.id),
            'invoice': str(order.id),
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
            'cancel_return': 'http://{}{}'.format(host, reverse('payment:cancelled')),
        }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'main/checkout.html', {'order': order, 'form':form})
