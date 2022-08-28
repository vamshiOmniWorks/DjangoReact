
from django.http import HttpResponse, JsonResponse



def index(request):
    return HttpResponse("Status 200K")
