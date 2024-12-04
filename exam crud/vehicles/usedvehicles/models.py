from django.db import models

# Create your models here.
class UsedVehicle(models.Model):

    title = models.CharField(max_length=200)

    owner_choices = (
        ("single owner","single owner"),
        ("second owner","second owner"),
        ("other","other")
    )

    owner_type = models.CharField(max_length=200,choices=owner_choices,default="single owner")

    running_kilometers = models.IntegerField()

    price = models.FloatField()

    fuel_choices=(
        ("petrol","petrol"),
        ("Diesel","Diesel"),
        ("EV","EV")
    )

    fuel_type = models.CharField(max_length=200,choices=fuel_choices,default="petrol")
