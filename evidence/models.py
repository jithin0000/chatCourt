from django.db import models

# Create your models here.
from customuser.models import MyUser
from case.models import Case

class Evidence(models.Model):
    """ model for evidence """
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(MyUser, related_name="evidence_owner",
                              null=True, blank=True
                              ,on_delete=models.CASCADE)
    case = models.ForeignKey(Case, related_name="evidence_case",null=True, blank=True, on_delete=models.CASCADE)
    content = models.FileField(upload_to="evidence/%Y/%m/%d/")

    crated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.case.case_number
