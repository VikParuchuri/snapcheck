from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from api.models import PhoneRecord
from django.http import Http404, HttpResponse
import json
import re

@cache_page(5 * 60)
def index(request):
    return render_to_response("index.html", {}, context_instance=RequestContext(request))

@cache_page(5 * 60)
def about(request):
    return render_to_response("about.html", {}, context_instance=RequestContext(request))

@csrf_exempt
def check(request):
    username = request.POST.get('username')
    number = request.POST.get('number')

    found = False
    message = "Awesome!  Your info is not in the leak."
    if username is not None and len(username) > 1:
        found = PhoneRecord.objects.filter(username=username).exists()
        if found:
            message = "Your username is in the leak.  You may want to consider changing it on other social networks."

    if number is not None and len(number) > 1 and not found:
        number = re.sub("[^0-9]", "", number)
        if len(number) > 7:
            found = PhoneRecord.objects.filter(phone_number="{0}XX".format(number[:8])).exists()
            if found:
                message = "Your phone number may be in the leak.  The last two digits of the numbers in the leak were removed.  Try with your username to be certain.  If your information is in the leak, you might want to consider changing your username on other social networks."

    return HttpResponse(json.dumps({
        'message': message,
        'found': found
    }))

