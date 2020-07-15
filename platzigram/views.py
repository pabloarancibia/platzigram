"""platzigram views."""
# django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime
import json
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    return HttpResponse('Server time {now}'.format(
        now=now
    ))

def sort(request):
    """hi."""
    #import pdb; pdb.set_trace()
    numbers = request.GET['numbers']
    numbers = [int(i) for i in numbers.split(',')]
    sorted_int = sorted(numbers)
    #response = JsonResponse(sorted_int, safe=False)
    data = {
        'status': 'ok',
        'numbers': sorted_int,
        'message': 'Integers Sorted'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type="application/json"
        )
def say_hi(request,name,age):
    """return """
    if age < 12:
        message = 'Sorry {}, you are not allowed'.format(name)
    else:
        message = 'hello {}'.format(name)
    return HttpResponse(message)