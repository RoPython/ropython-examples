from rest_framework.permissions import IsAuthenticated

class AuthenticatedOrDefault(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in ('HEAD', 'OPTIONS'):            
            return True
        return super().has_permission(request, view)