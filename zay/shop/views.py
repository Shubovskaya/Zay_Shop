
from django.http import HttpRequest, HttpResponse


def error404(request, exception):
    return HttpResponse('<b>404</b>')









