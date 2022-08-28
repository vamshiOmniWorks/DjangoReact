
import sys
import traceback
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from polls.models import Gender


# Create your views here.
@require_http_methods(["GET"])
def get_gender(request):
    try:
        gender_list = list(Gender.objects.values())
        return JsonResponse(gender_list, safe=False)
    except:
        e = sys.exc_info()[0]
        print("exception", e)
        traceback.print_exc()
        return JsonResponse({"message": "Oops! Something went wrong. Please try again later.", "status": "Error"})
