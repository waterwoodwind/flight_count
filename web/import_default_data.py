#coding=utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flight_count.settings")


import django
django.setup()

from beijing_flight_count.models import *

def import_model(txt_file,model_object):
    f = open(txt_file)
    txt = f.read()
    f.close()
    objectList = []
    title = txt.split('，')
    print title
    for item in title:
        single_object = model_object(name=item)
        objectList.append(single_object)
    model_object.objects.bulk_create(objectList)

def import_actual_begin():
    ac_all = Ac_Number.objects.all()
    for ac in ac_all:
        loc = Location.objects.get(name=u"重庆")
        check = Check_Option.objects.get(name=u"是")
        ActualTimetable.objects.create(actual_ac_number=ac,
                                       actual_date="2017-03-24",
                                       actual_location=loc,
                                       actual_scheduled_check=check)

def import_plan_begin():
    ac_all = Ac_Number.objects.all()
    for ac in ac_all:
        loc = Location.objects.get(name=u"重庆")
        check = Check_Option.objects.get(name=u"是")
        PlanTimetable.objects.create(plan_ac_number=ac,
                                       plan_date="2017-04-01",
                                       plan_location=loc,
                                       plan_scheduled_check=check)

if __name__ == "__main__":
    import_plan_begin()
    print('Done!')