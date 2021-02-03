from django.http import HttpResponse
from .models import Db

def index(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Db.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')