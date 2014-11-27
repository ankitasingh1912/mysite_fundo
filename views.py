__author__ = 'ANKITA'

from django.http import HttpResponse
import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><head>Hello, world. Ankita Rocks</head><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
