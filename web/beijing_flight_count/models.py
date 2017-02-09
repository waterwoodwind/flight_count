# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


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
