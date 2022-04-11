from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid
from datetime import date
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
    user_registration = models.DateField(blank=False, today=date.today())
    userDateOfBirth = models.DateField()


class TourGuide(models.Model):
    # tourExp = models.OneToManyField(TourExperience, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guideFirstName = models.CharField(max_length=50)
    guideLastName = models.CharField(max_length=50)
    guideDescription = models.TextField(max_length=300)
    # guidePicture = models.ImageField(upload_to='uploads/')
    # guideRating = models.IntegerField()


class TourExperience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tourTitle = models.CharField(max_length=100)
    tourLocation = models.CharField(max_length=50)
    tourDuration = models.IntegerRangeField(range(60, 300))
    tourPrice = models.FloatField()
    tourAvailableDate = models.DateField()
    tourMaxNumberOfPeople = models.IntegerRangeField(range(0, 30))
    tourDescription = models.TextField(max_length=300)
    # tourCategory = models.CharField(max_length=50)
    tourGuide = models.ForeignKey(TourGuide, on_delete=models.CASCADE)
