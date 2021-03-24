from django.db import models

# Create your models here.


class Member(models.Model):
    Sr_No = models.AutoField(primary_key=True)

    FROM = (
        ('Delhi', 'Delhi'), ('Mumbai', 'Mumbai'),
        ('Bangalore', 'Bangalore'), ('Bhopal', 'Bhopal'), ('Pune', 'Pune'),
    )

    TO = (
        ('Delhi', 'Delhi'), ('Mumbai', 'Mumbai'),
        ('Bangalore', 'Bangalore'), ('Bhopal', 'Bhopal'), ('Pune', 'Pune'),
    )

    NO_OF_PASSENGERS = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('>5', '>5'),
    )
    DESTINATION = models.CharField(max_length=50,
                                   choices=FROM, null=True, blank=True)
    ARRIVAL = models.CharField(max_length=50,
                               choices=TO, null=True, blank=True)
    PASSENGERS = models.IntegerField(
        choices=NO_OF_PASSENGERS, null=True, blank=True)

    Airlines = models.CharField(
        max_length=500, blank=True, null=True)
    Depart_time = models.CharField(
        max_length=500, blank=True, null=True)
    Arrival_time = models.CharField(
        max_length=500, blank=True, null=True, )
    Fare = models.IntegerField(blank=True,
                               null=True, default=0)
    Date = models.IntegerField(blank=True,null=True)

class Contact(models.Model):
    Sr_No = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    message = models.TextField(max_length=100, blank=True)
    Time = models.DateTimeField(auto_now_add=True, blank=True)


class Email(models.Model):
    email = models.CharField(max_length=50, blank=True)
