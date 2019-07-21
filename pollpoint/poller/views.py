from django.shortcuts import render
from .models import Poll, PollOption, PollChoice, SessionUser
import random

def index(request):
    # if request.session.get("has_voted", False):
    #     polls = Poll.objects.all()
    #     poll = random.choice([poll for poll in polls])
    return render(request, 'poller/error.html', {})
