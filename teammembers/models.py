from django.db import models
from django.urls import reverse
# Create your models here.


class TeamMember(models.Model):
	# Model with 6 fields listed below
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	phone = models.CharField(max_length=120)
	admin_status = models.BooleanField(blank=True, default=False)
	# Used this field early on, had trouble running code without having this set to null=True
	delet = models.CharField(max_length=120, blank=True, default=False,null=True)

	


	