from django.contrib.auth.models import User

class LoginAsBackend(object):
    def authenticate(self, from_user, to_username):
        if not from_user.is_superuser:
            return None
        try:
            user = User.objects.get(username=to_username)
        except User.DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None