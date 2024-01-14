from django.db import models

class Calls(models.Model):
    month = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    percentage_change = models.IntegerField(default=0)

class Messages(models.Model):
    month = models.CharField(max_length=20)
    count = models.IntegerField(default=0)

class PeopleAskedForDirection(models.Model):
    month = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    percentage_change = models.IntegerField(default=0)

class WebsiteVisitsFromProfile(models.Model):
    month = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    percentage_change = models.IntegerField(default=0)

class ProfileViews(models.Model):
    month = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    percentage_change = models.IntegerField(default=0)

class SearchesAppearance(models.Model):
    month = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    percentage_change = models.IntegerField(default=0)
