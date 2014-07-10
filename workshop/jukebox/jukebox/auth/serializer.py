""" Contains a serialization class used for
serializing tokens.
"""

from rest_framework.serializers import ModelSerializer, Field

from .models import AuthToken

class TokenSerializer(ModelSerializer):
    user = Field(source='user_info')
    
    class Meta:
        model = AuthToken
        lookup_field = "key"
           