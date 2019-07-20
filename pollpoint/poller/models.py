from django.db import models

class Poll(models.Model):
    title = models.TextField()
    description = models.TextField()

class PollOption(models.Model):
    title = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

class SessionUser(models.Model):
    first_connected = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField()

    def has_voted(self):
        return len(PollChoice.objects.filter(user=self)) > 0

class PollChoice(models.Model):
    option = models.ForeignKey(PollOption, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(SessionUser, on_delete=models.CASCADE)