from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.conf import settings
import jwt

class JWTBackend(BaseBackend):
    def authenticate(self, request, token=None):
        try:
            payload=jwt.decode(token,settings.SECRET_KEY)
            user=User.objects.get(id=payload["id"],username=payload["username"])
            if user.is_active: return user
        except: pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None