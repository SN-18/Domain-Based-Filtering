#@author: Saurabh Nanda
#unity Id: snanda2@ncsu.edu
#contains main program logic

#a brief description of parse_har_fld and parse_har_url:
#parse_har_fld parses har files, returns the list of fld's of all the url's
#parse har file is modified to return the list of all the url's

import parse_har_fld,parse_har_url
from tld import get_fld

#has the fld for all the urls, used in Q1 and Q2
url_list_fld1=parse_har_fld.main("www.cnn.com.har")
url_list_fld2=parse_har_fld.main("www.macys.com.har")

#returns the list of [mimetype,url] as individual elements, used in Q3
url_mimetype_list1=parse_har_url.main('www.cnn.com.har')
url_mimetype_list2=parse_har_url.main('www.macys.com.har')

count1=0
count2=0

s1=set()
s2=set()

for url in url_list_fld1:
    if 'cnn.com' not in url:
        s1.add(url)
        count1= count1 + 1

for url in url_list_fld2:
    if 'macys.com' not in url:
        s2.add(url)
        count2=count2+1

s1_li=list(s1)
s2_li=list(s2)

print("This is Questin 2(a) for HW-3\n")

print("Number of urls that are not cnn.com, and are third party domains for www.cnn.com.har:", len(s1))
print("The first five elements for third-party url's for www.cnn.har file are:")

for i in range(5):
    print(s1_li[i],sep=" ")
print('\n')

print("Number of urls that are not macys.com, and are third party domains for www.macys.com.har:", len(s2))
print("The first five elements for third party url's in macy'scom.har are:\n")

for i in range(5):
    print(s2_li[i],sep=" ")
print("\n")

print("#End of question 2(a)#\n\n")
#end of question 2(a)


#Code for Question 2(b)

print("This is question 2(b) for HW3")
intersection_s1_s2=s1.intersection(s2)
num=len(intersection_s1_s2)
print("The number of third party domains that exist in both har files for macys.com and cnn.com datasets are:",num)
print("\nThe elements present in intersection are printed as follows, for reference:")
print(intersection_s1_s2)
print("#End of Question 2(b)#\n\n")



#Question 2 (c)

import json
file=open('disconnect.json',encoding='utf8')
data=json.load(file)

keys_data=data['categories'].keys()
list_of_domains=list()

#Parsing Nested Dictionaries in Disconnected.json file
for i in keys_data:
    list_of_dicts=data['categories'][i]
    for d in list_of_dicts:
        keys=d.keys()
        for j in keys:
            temp_dict=d[j]
            for element in temp_dict:
                list_of_domains.append(get_fld(element,fail_silently=True))


#contains the list of domains in disconnected.json
domain_set_disconnect=set(list_of_domains)




print("This is the length of unique url's in disconnect.json ",len(domain_set_disconnect))
x=domain_set_disconnect.intersection(s1)
y=domain_set_disconnect.intersection(s2)

print("Number of Blocked Domains if we use disconnect as a filter list on list www.cnn.com.har are:",len(x))
print("Number of Blocked Domains if we use disconnect as a filter list on list www.macys.com.har are:",len(y))
print("\n\n")
file.close()
print("#End of Question 2(c)#")
#End of Question 2(c)


#Code for Question 3
from adblockparser import AdblockRules

#make a txt_file variable for file called raw rules, which contains filtering rules provided to us in question
txt_file=open("raw_rules","r")
file_content=txt_file.read()

#split the content_list rules
content_list=file_content.split("\n")
rules=AdblockRules(content_list)

#initialize a list for the url's that are blocked in har files for cnn and macy's, based on adblock rules
blocked_in_cnn=list()
blocked_in_macys=list()

print("This is question number 3\n")

#Code for printing blocked urls in www.cnn.com.har, based on adblock rules
print("Below, we print the number of blocked urls in www.cnn.com.har based on adblock rules")
for url_m in url_mimetype_list1:
    rule_url_li = []
    image_flag=False
    third_party_flag=False
    script_flag=False

    mimetype=url_m[1]
    url=url_m[0]

    if "cnn" not in url:
        third_party_flag=True
        rule_url_li.append("Third-Party-Domain")

    if "image" in str(mimetype):
        image_flag=True
        rule_url_li.append("Image")

    if "javascript" in str(mimetype):
        script_flag=True
        rule_url_li.append("Script")


    #list of options, to be passed to rules.should_block(url_name,options) in the next line
    options={'image':image_flag,'third-party':third_party_flag,'script':script_flag}

    if rules.should_block(url,options):
        url_fld=get_fld(url, fail_silently=True)
        blocked_in_cnn.append(rule_url_li)
        # temp_string=temp_string+ str(url_fld)

        # append list of (flags used plus url blocked) to list called blocked in cnn
        # blocked_in_cnn.append(temp_string)



#Code for printing blocked urls in www.macys.com.har, based on adblock rules
print("\n")
print("Below, we print the number of blocked urls in www.macys.com.har based on adblock rules")

print("\nTotal number of url's blocked in har file for cnn, with corresponding adblock rule and their domains (fld) are:",len(blocked_in_cnn))
for element in blocked_in_cnn:
    print(element)

for url_m in url_mimetype_list2:
    rule_url_li=[]
    image_flag=False
    third_party_flag=False
    script_flag=False

    mimetype=url_m[1]
    url=url_m[0]

    if "macys" not in url:
        third_party_flag=True
        rule_url_li.append("Third-Party-Domain")
    if "image" in str(mimetype):
        image_flag=True
        rule_url_li.append("Image")
    if "javascript" in str(mimetype):
        rule_url_li.append("Script")
        script_flag=True


    options={'image':image_flag,'third-party':third_party_flag,'script':script_flag}

    if rules.should_block(url,options):
        url_fld=get_fld(url, fail_silently=True)
        rule_url_li.append(url_fld)
        print(rule_url_li)
        # append list of (flags used plus url blocked) to list called blocked in macys
        blocked_in_macys.append(rule_url_li)

#


print("\nTotal number of url's blocked in har file for macy's, with corresponding ad-block rules and their domains (fld) are:",len(blocked_in_macys))
for element in blocked_in_macys:
    print(element)












