"""Platzigram URLs modulde."""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

"""Return a greeting."""
def hello_world(request):
    return HttpResponse('Hello World')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello-world', hello_world)
]
