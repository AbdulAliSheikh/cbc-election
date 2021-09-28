from django.db import models


class DatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Voter(DatedModel):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    GENDER_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    ]
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    cnic = models.BigIntegerField(unique=True)
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
    )
    phase = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
