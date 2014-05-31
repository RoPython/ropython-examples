
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .models import AuthToken
from .serializer import TokenSerializer
from ..permission import AuthenticatedOrDefault

class AuthCreate(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        if 'HTTP_X_REAL_IP' in request.META:
            created_by_host = request.META['HTTP_X_REAL_IP']
        else:
            created_by_host = request.META['REMOTE_ADDR']
        token_key = AuthToken.generate_key()
        user, _ = User.objects.get_or_create(username=created_by_host)
        token = AuthToken.objects.create(
            host=created_by_host, user=user, key=token_key)
        token.save()        
        return Response(TokenSerializer(token).data,
                        status=status.HTTP_201_CREATED)

class AuthTokenList(generics.ListAPIView):
    serializer_class = TokenSerializer
    permission_classes = (AuthenticatedOrDefault, )
    queryset = AuthToken.objects.all()

    def get_queryset(self):
        """
        This view should return a list of all the tokens
        for the currently authenticated user.
        """
        return (AuthToken.objects
                         .filter(user=self.request.user)
                         .order_by('-created'))

