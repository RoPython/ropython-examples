""" Implements a simple token based authentication. """
from rest_framework.authentication import BasicAuthentication
from django.http import Http404
from django.core.exceptions import PermissionDenied

from .models import AuthToken
         
class APITokenAuthentication(BasicAuthentication):
    """
    Token-based authentication.
    """
    def authenticate(self, request):
        """ Authenticate method.

        :param `request:
            The HTTP request
        :returns:
            A tuple, where the first item is the authenticated user.         
        :raises:
            :exc:`AuthenticationFailed` for various reasons
        """
        jukebox_token = request.META.get('HTTP_X_JUKEBOX_TOKEN')
        if jukebox_token:
            try:
                token = AuthToken.objects.get(key=jukebox_token)
            except AuthToken.DoesNotExist:
                raise Http404('Unknown token')

            return (token.user, token)
        return (None, None)
