from django.shortcuts import render, redirect
from .models import Poll, PollOption, PollChoice, SessionUser
from django.contrib.auth.decorators import login_required
import random

def index(request):
    if request.session.get("user_obj", None) == None:
        request.session["user_obj"] = SessionUser.objects.create(user_agent=request.META['HTTP_USER_AGENT'])
    if request.session.get("user_obj").has_voted:
        return redirect("/connect")
    else:
        polls = Poll.objects.filter(active=True)
        poll = random.choice([poll for poll in polls])
        return render(request, 'poller/vote.html', {
            "poll": poll,
            "issue": request.GET.get("issue", False)
        })

def connect(request):
    if request.session.get("user_obj", None) == None:
        return redirect("/")
    if not request.session.get("user_obj").has_voted:
        choice = request.POST.get("choice", None)
        if choice != None:
            PollChoice.objects.create(user=request.session.get("user_obj"), option=PollOption.objects.get(id=int(choice)))
        else:
            return redirect("/?issue=True")
    return redirect("/error")

def error(request):
    return render(request, "poller/error.html")

@login_required
def stats(request):
    return render(request, "poller/stats.html", {
        "polls": Poll.objects.all(),
        "sessions": SessionUser.objects.all().order_by("-first_connected")
    })