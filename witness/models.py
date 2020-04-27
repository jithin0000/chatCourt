from django.db import models

# Create your models here.
from django.urls import reverse

from case.models import Case
from customuser.models import MyUser


class Witness(models.Model):
    """ model for witness """
    user = models.ForeignKey(MyUser,related_name="witness_profile", on_delete=models.CASCADE)
    added_by = models.ForeignKey(MyUser,related_name="added_by", on_delete=models.CASCADE,
                                 null=True, blank=True)
    case = models.ForeignKey(Case,related_name="wit_case", on_delete=models.CASCADE,
                             null=True, blank=True)

    profile_pic = models.ImageField(upload_to="witness/%Y/%m/%d/", null=True, blank=True)
    phone_number = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('witness_profile', kwargs={'pk': self.user.id})

    def __str__(self):
        return self.user.username

