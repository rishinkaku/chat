from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request,*args,**kwargs):
    print(request.user,request.user.is_authenticated)
    return HttpResponse()