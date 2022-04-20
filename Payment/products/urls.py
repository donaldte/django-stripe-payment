from django.urls import path
from .views import (
    ProductLandingPageView,
    CreateCheckoutSession,
    SuccessView,
    CancelView,
)

urlpatterns = [
    path('', ProductLandingPageView.as_view(), name='product-landing-page'),
    path('create-checkout-session/<pk>', CreateCheckoutSession.as_view(), name='create-checkout-session'),
    path('/success', SuccessView.as_view(), name='success'),
    path('/cancel', CancelView.as_view(), name='cancel'),
]
