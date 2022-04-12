from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

#---- NEEDS TO REMAKE THE MODELS ----#

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('end_user', 'end_user'),
        ('tour_guide', 'tour_guide'),
        ('moderator', 'moderator'),
    )
    user_type = models.CharField(max_length=50,
                                 choices=USER_TYPE_CHOICES, null=True)


class EndUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userFirstName = models.CharField(max_length=50)
    userLastName = models.CharField(max_length=50)
    user_registration = models.DateField(blank=False)
    userDateOfBirth = models.DateField()


class TourGuide(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guideFirstName = models.CharField(max_length=50)
    guideLastName = models.CharField(max_length=50)
    guideDescription = models.TextField(max_length=300)


class TourExperience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tourTitle = models.CharField(max_length=100)
    tourLocation = models.CharField(max_length=50)
    tourDuration = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )
    tourPrice = models.FloatField()
    tourAvailableDate = models.DateField()
    tourMaxNumberOfPeople = models.IntegerField()
    tourDescription = models.TextField(max_length=300)
    tourGuide = models.ForeignKey(TourGuide, on_delete=models.CASCADE)
