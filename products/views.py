import stripe
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView

from products.models import Product, StripeCheckoutSession

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': product.stripe_price_data,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.DOMAIN + reverse('success') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.DOMAIN + reverse('cancel'),
        )

        StripeCheckoutSession.objects.create(
            stripe_id=checkout_session.stripe_id,
            product=product,
            status=checkout_session['status']  # have to be 'open'
        )

        return redirect(checkout_session.url)


class Products(ListView):
    model = Product
    template_name = 'home.html'


class SuccessView(TemplateView):
    template_name = 'success.html'

    def get(self, request, *args, **kwargs):
        stripe_session = get_object_or_404(StripeCheckoutSession, stripe_id=request.GET.get('session_id'))

        session = stripe.checkout.Session.retrieve(stripe_session.stripe_id)

        stripe_session.customer_email = session['customer_details']['email']
        stripe_session.status = session['status']
        stripe_session.save()

        return super().get(request, args, kwargs)


class CancelView(TemplateView):
    template_name = 'cancel.html'
