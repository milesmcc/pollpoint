from django.shortcuts import render

def index(request):
    return render(request, 'poller/base.html', {})
