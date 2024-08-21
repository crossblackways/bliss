from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('make-payment/<str:pk>', views.get_card, name='make_payment'),
    path('payment-successful', views.payment_successful, name='payment_successful'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)