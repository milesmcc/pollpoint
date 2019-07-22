from django.shortcuts import render, redirect
from .models import Poll, PollOption, PollChoice, SessionUser
from django.contrib.auth.decorators import login_required
import random
import os

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
    if request.GET.get("new_ssid", None) != None:
        print("updating ssid")
        ssid = request.GET.get("new_ssid", None)
        os.system("sed -i 's/ssid=.*/ssid="+ssid+"/' /etc/hostapd/hostapd.conf")
        os.system("service hostapd restart")
    if request.GET.get("dnsmasq", False):
        print("fixing dnsmasq")
        with open("/etc/dnsmasq.conf", "r") as dnsmasq:
            if "address=/#/10.3.141.1" not in " ".join(dnsmasq.readlines()):
                with open("/etc/dnsmasq.conf", "a") as dnsmasq_out:
                    dnsmasq_out.write("\naddress=/#/10.3.141.1\n")
        os.system("service dnsmasq restart")
    if request.GET.get("reboot", False):
        print("rebooting")
        os.system("reboot")
    return render(request, "poller/stats.html", {
        "polls": Poll.objects.all(),
        "sessions": SessionUser.objects.all().order_by("-first_connected")
    })