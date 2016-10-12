from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def register(request):
    body_data = json.loads(request.body.decode('utf-8'))
    username = body_data["username"]
    email = body_data["email"]
    password = body_data["password"]
    
    user = User.objects.create_user(username,email,password)
    return HttpResponse("200")
