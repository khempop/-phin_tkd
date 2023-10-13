from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Subscribers
#from . forms import *
from django.contrib import messages
from django.shortcuts import render
import stripe
import json
from django.conf import settings

stripe.api_key = settings.TEST_STRIPE_SECRET_KEY

class AppsView(LoginRequiredMixin,TemplateView):
    pass

# Subscriber
# path("subscriber/purchase", view=subscribers_purchase_view, name="subscribers.purchase"),
# path("subscriber/checkout", view=subscribers_checkout_view, name="subscribers.checkout"),
# path("subscriber/status", view=subscribers_status_view, name="subscribers.status"),
subscribers_purchase_view = AppsView.as_view(template_name="apps/subscriber/subscribers-purchase-view.html")
#subscribers_checkout_view = AppsView.as_view(template_name="apps/subscriber/subscribers-checkout-view.html")
subscribers_status_view = AppsView.as_view(template_name="apps/subscriber/subscribers-status-view.html")
subscribers_success_view = AppsView.as_view(template_name="apps/subscriber/subscribers-status-view.html")
subscribers_cancel_view = AppsView.as_view(template_name="apps/subscriber/subscribers-status-view.html")

def subscribers_checkout_view(request):
    if request.method == 'POST':
        try:
            prices = stripe.Price.list(
                lookup_keys=[request.POST.get("lookup_key","")],
                expand=['data.product']
            )
            print(prices.data[0].id)
            checkout_session = stripe.checkout.Session.create(
                [
                    {
                        'price': prices.data[0].id,
                        'quantity': 1,
                    },
                ],
                'subscription',
                settings.SITE_DOMAIN +
                '/subscribers/subscriber/success/{CHECKOUT_SESSION_ID}',
                settings.SITE_DOMAIN + '/subscribers/subscriber/cancel',
            )
            return redirect(checkout_session.url, status_code=303)
        except Exception as e:
            print(e)
            return redirect('/', status=500)
