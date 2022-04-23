from django.urls import path
from .views import signup, log_in, log_out

urlpatterns = [
    path('', log_in, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', log_out, name='logout'),
]