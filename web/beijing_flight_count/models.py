# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ac_Number(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)

    def __unicode__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)

    def __unicode__(self):
        return self.name

class Check_Option(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)

    def __unicode__(self):
        return self.name


class BeijingFlights(models.Model):
    date = models.DateField(u'日期')
    flight_number = models.CharField(max_length=20,
                                     verbose_name=u'航班号')
    ac_number = models.CharField(max_length=10,
                                 verbose_name=u'机号')
    departure_airfield = models.CharField(max_length=20,
                                          verbose_name=u'起飞机场')
    departure_datetime = models.DateTimeField(verbose_name=u'起飞时间')
    arrival_datetime = models.DateTimeField(verbose_name=u'落地时间')
    arrival_airfield = models.CharField(max_length=20,
                                        verbose_name=u'落地机场')

class ActualTimetable(models.Model):
    actual_ac_number = models.ForeignKey(Ac_Number,
                                 verbose_name=u'机号')
    actual_date = models.DateField(u'日期')
    actual_location = models.ForeignKey(Location,verbose_name=u'地点')
    actual_scheduled_check = models.ForeignKey(Check_Option, verbose_name=u'是否定检')

class PlanTimetable(models.Model):
    plan_ac_number = models.ForeignKey(Ac_Number,
                                 verbose_name=u'机号')
    plan_date = models.DateField(u'日期')
    plan_location = models.ForeignKey(Location,verbose_name=u'地点')
    plan_scheduled_check = models.ForeignKey(Check_Option, verbose_name=u'是否定检')