from django.urls import path

from . import views

urlpatterns = [
    path('place_order/', view=views.place_order, name='place_order'),
    path('payments/', view=views.payments, name='payments'),
    path('order_complete/', views.order_complete, name="order_complete")
]
