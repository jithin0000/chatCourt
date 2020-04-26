from django.db import models

# Create your models here.
from customuser.models import MyUser
from case.models import Case

class MessageManager(models.Manager):
    """ manager for message """
    def last_10_messages(self, caseNumber):
        return self.filter(case__case_number=caseNumber).order_by('-timestamp').all()[:10]

class Message(models.Model):
    """model for chat"""

    author = models.ForeignKey(MyUser, related_name="from_user", on_delete=models.CASCADE)
    case = models.ForeignKey(Case, related_name="case", on_delete=models.CASCADE)
    message = models.CharField(max_length=155)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = MessageManager()

    def __str__(self):
        return self.message

