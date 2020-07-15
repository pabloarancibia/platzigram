from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime
posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yesica',
        'timestamp': datetime.now().strftime('%b %dth, %Y'),
        'picture': 'https://picsum.photos/200/200/?image=1036',        
    }
]

def list_posts(request):
    content = []
    for post in posts:
        content.append("""
        <p>{name}</p>
        """.format(**post))
    return HttpResponse('br'.join(content))
