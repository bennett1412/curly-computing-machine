from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class STGUserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('Donor','Donor'),
        ('NGO', 'NGO'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES)
    Location = models.TextField(max_length=600)
    Pincode = models.PositiveIntegerField()
