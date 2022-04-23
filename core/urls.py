from django.urls import path, include
from . import views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', include(('customer.urls', 'customer'), namespace='customer'))
]
