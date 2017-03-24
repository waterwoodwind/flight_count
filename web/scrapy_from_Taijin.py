#coding=utf-8
from flight_count.wsgi import *
from beijing_flight_count.models import BeijingFlights
import requests
import urllib
import re

params = {
    'from_date':'20170211',
    'to_date':'20170213',
    'dep_apt':'',
    'arr_apt':'',
    'flt_id':'',
    'ac_id':'',
    'ac_TYPE':'',
    'ac_STOP':'',
    'D3':'6',
    'ac_type_kuan':'重庆'
}
post_data = urllib.urlencode(params)

r = requests.post("http://10.10.102.102/oracle/busi_his_flt_query.asp", data=params)
r.encoding = 'gb2312'
res = r.text
#print(res)

pattern = re.compile(r'<table border=1.*>(\n|.)*</table>')
match = re.search(pattern, res)
if match:
    print type(match.group())
    #print match.group()
    table_str = match.group()
else:
    print '未找到'
    exit()

pattern_tr = re.compile(r'<tr bgColor=#ACDEA4.*?</tr>', re.S)
match_tr = re.findall(pattern_tr, table_str)

#for item in match_tr:
#    print item
print len(match_tr)
pattern_td = re.compile(r'<td.*?>.*?</td>', re.I | re.S)

pattern_sub = re.compile(r'<.*?>')
list_flt_table = []
list_index = [0,2,3,5,8,9,10]
for td in match_tr:
    match_td = re.findall(pattern_td, td)
    list_td = []
    for index, item in enumerate(match_td):
        #print item
        match_sub = re.sub(pattern_sub, "", item)
        match_td[index] = match_sub.strip()
        if index in list_index:
            list_td.append(match_td[index])
    list_flt_table.append(list_td)
    print "列数：%s"%(len(match_td))

list_del_table = []
for index,item in  enumerate(list_flt_table):
    if item[2] == u'航班取消':
        continue
    elif item[3] <> u'PEK' and item[6] <> u'PEK':
        continue
    else:
        list_del_table.append(item)

querysetlist = []
for index, item in enumerate(list_del_table):
    print index, item
    querysetlist.append(BeijingFlights(date=item[0],
                                       flight_number=item[1],
                                       ac_number=item[2],
                                       departure_airfield=item[3],
                                       departure_datetime=item[4],
                                       arrival_datetime=item[5],
                                       arrival_airfield=item[6]))

BeijingFlights.objects.bulk_create(querysetlist)

'''
pattern_td = re.compile(r'>.+<')
match_td = re.findall(pattern_td, table_str)
for item in match_td:
    print item
'''