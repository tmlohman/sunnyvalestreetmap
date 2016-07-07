
# coding: utf-8

# Ways Audit
# - Id, uid, version, and changeset should be integers
# - Timestamp should be in correct format
# - Timestamp should be before download date/time
# - Way Ids should be unique
# 

# In[1]:

import os
os.getcwd()


# In[11]:

# All nodes should be defined exactly once, and can be typed as integers
import csv
f = open('ways_complete.csv', 'r')
ways = csv.DictReader(f)

ways_set = set()
repeated_ways = {}

def check_ways_set(way, ways_set, repeated_ways):
    n = int(way['id'])
    if n not in ways_set:
        ways_set.add(n)
    else:
        repeated_ways[n] += 1
    return repeated_ways
     
for way in ways:
    check_ways_set(way, ways_set, repeated_ways)

print len(ways_set)
print len(repeated_ways)

# There are 54,887 ways, and none are repeated


# In[13]:

import csv
f = open('ways_complete.csv', 'r')
ways = csv.DictReader(f)

def check_type(data):
    try:
        int(data)
    except:
        print data
        
for way in ways:
    check_type(way['id'])
    check_type(way['uid'])
    check_type(way['changeset'])
    check_type(way['version'])
    
# All ids, uids, versions, and changesets are integers


# In[20]:

import csv
f = open('ways_complete.csv', 'r')
ways = csv.DictReader(f)

i = 0
w = 0
for way in ways:
    if 'changeset'in way.keys():
        i += 1
    w += 1

print i
print w


# In[9]:

# Time and date should be in standard format
import re
import csv

f = open('ways_complete.csv', 'r')
ways = csv.DictReader(f)

date_time = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")

for way in ways:
    try:
        date_time.match(way['timestamp'])
    except:
        print way['timestamp']
    
# All times and dates are in standard format


# In[10]:

# All timestamps should have occurred before the file was downloaded
import csv
f = open('ways_complete.csv', 'r')
ways = csv.DictReader(f)
download_date_time = "2016-06-17T15:49:00Z" # File was downloaded at 8:49AM PST on 6/17/16


for way in ways:
    if way['timestamp'] >= download_date_time:
        print way['timestamp']

# All timestamps occured before download
        

