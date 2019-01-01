from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    update_date = models.DateField(null=True, blank=True)
    create_date = models.DateField(null=True, blank=True)

# queen / queenpassword / queen@queen.com
