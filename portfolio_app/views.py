from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def landing_page(request):
    return render(request, 'landing_page.html',{})
    
# Create your views here.
