#coding=utf-8
import requests
import urllib
import re

params = {
    'from_date':'20170119',
    'to_date':'20170119',
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
list_index = [0,3,5,8,9,10]
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

for index,item in  enumerate(list_flt_table):
    print index, item


'''
pattern_td = re.compile(r'>.+<')
match_td = re.findall(pattern_td, table_str)
for item in match_td:
    print item
'''