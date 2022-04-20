import stripe
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
from .models import Products

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
class CancelView(TemplateView):
    template_name = 'success.html'

class SuccessView(TemplateView):
    template_name = 'cancel.html'


class ProductLandingPageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        product = Products.objects.get(name='Testproduct')
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)

        context.update({
            'product':product,
        })
        return context

class CreateCheckoutSession(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'http://127.0.0.1:8000' 
        product_id = self.kwargs['pk']
        product = Products.objects.get(id=product_id)
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': product.id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success',
                cancel_url=YOUR_DOMAIN + '/cancel',
            )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)

# if __name__ == '__main__':
#     app.run(port=4242)