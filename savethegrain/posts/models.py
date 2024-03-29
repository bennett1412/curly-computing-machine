from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField(default=timezone.now)
    Donor = models.ForeignKey(User, on_delete=models.CASCADE)
    food_quantity = models.PositiveIntegerField(default=0)
    # NGO = models.OneToOneField(User,default="NULL")

    # def get_absolute_url(self):
    #     return reverse('blog:post-detail', kwargs={'pk':self.pk})
    