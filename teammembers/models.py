from django.db import models
from django.urls import reverse
# Create your models here.


class TeamMember(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	phone = models.CharField(max_length=120)
	admin_status = models.BooleanField(blank=True, default=False)

	


	