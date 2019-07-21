from django.db import models
import random

class Poll(models.Model):
    title = models.TextField()
    active = models.BooleanField(default=True)

    @property
    def options(self):
        return PollOption.objects.filter(poll=self)

    @property
    def options_sorted(self):
        return sorted(self.options, key=lambda k: k.votes, reverse=True)

    @property
    def total_votes(self):
        return sum([len(PollChoice.objects.filter(option=option)) for option in self.options])

    def __str__(self):
        return self.title

class PollOption(models.Model):
    title = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    @property
    def votes(self):
        return len(PollChoice.objects.filter(option=self))

    @property
    def vote_ratio(self):
        return self.votes*100/self.poll.total_votes

class SessionUser(models.Model):
    first_connected = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField()

    @property
    def has_voted(self):
        return len(PollChoice.objects.filter(user=self)) > 0

class PollChoice(models.Model):
    option = models.ForeignKey(PollOption, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(SessionUser, on_delete=models.CASCADE)