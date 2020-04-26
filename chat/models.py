from django.db import models

# Create your models here.
from customuser.models import MyUser
from case.models import Case

class Message(models.Model):
    """model for chat"""

    author = models.ForeignKey(MyUser, related_name="from_user", on_delete=models.CASCADE)
    case = models.ForeignKey(Case, related_name="case", on_delete=models.CASCADE)
    message = models.CharField(max_length=155)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]