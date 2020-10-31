from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class STGUser(User):
    USER_TYPE_CHOICES = (
        ('Donor','Donor'),
        ('NGO', 'NGO'),
    )

    user_type = models.CharField(choices=USER_TYPE_CHOICES)
    Location = models.TextField(max_length=600)
    Email = models.EmailField()
