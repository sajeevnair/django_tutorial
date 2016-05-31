import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import pusher
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

p = pusher.Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET,

)


def index(request):
    return render(
        request,
        'notifications/index.html',
        {'PUSHER_KEY': settings.PUSHER_KEY, 'CHANNEL_NAME':settings.CHANNEL_NAME}
    )


def message(request):
    msg = request.POST['user_message']

    p.trigger(settings.CHANNEL_NAME, 'private-message', {'user_message': msg})
    return HttpResponse('')

@csrf_exempt
def auth(request):
    channel_name = request.POST['channel_name']
    socket_id = request.POST['socket_id']
    auth = p.authenticate(channel_name, socket_id)
    return HttpResponse(json.dumps(auth))