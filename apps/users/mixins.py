from rest_framework import status
import datetime
from gd_backend.helpers.errror_response import error_response
from .models import User


#Add this mixin to the login-required classes

class CustomLoginRequiredMixin():

    def dispatch(self, request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return error_response('Please set Auth-Toke.', status.HTTP_401_UNAUTHORIZED)
        
        token= request.headers['Authorization']
        now= datetime.datetime.now()
        login_user= User.objects.filter(token=token, token_expires__gt=now)

        if len(login_user)==0:
            return error_response('This token is invalid or expired already', status.HTTP_401_UNAUTHORIZED)
        
        request.login_user=login_user[0]
        return super().dispatch(request, *args, **kwargs)