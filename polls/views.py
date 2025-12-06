from django.http import HttpResponse
import datetime
import logging

logger = logging.getLogger(__name__)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def my_custom_page_not_found_view(request, exception):
    logger.error("Something went wrong!")
    return HttpResponse("Custom 404 Page", status=404)