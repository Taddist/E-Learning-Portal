from rest_framework import viewsets

from students.models import User 
from api.serializers import UserSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
	queryset=User.objects.order_by('-date_joined')
	serializer_class=UserSerializer