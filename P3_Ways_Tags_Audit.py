
# coding: utf-8

# Auditing Ways Tags file:
# - Id should be an integer, and should be in Ways file
# - Each tag should have exactly 4 fields

# In[1]:

import os
os.getcwd()


# In[2]:

import csv
f = open('ways_tags_complete.csv', 'r')
ways_tags = csv.DictReader(f)
f2 = open('ways_complete.csv', 'r')
ways = csv.DictReader(f2)

known_ways = set()
for way in ways:
    known_ways.add(way['id'])
    
known_ways = sorted(known_ways)


for tag in ways_tags:
    t = tag['id']
    if t not in known_ways:
        print tag
        
# All tags are in known_ways, since all ways are integers, this check is also satisfied.


# In[3]:

import csv
f = open('ways_tags_complete.csv', 'r')
ways_tags = csv.DictReader(f)

bad_tags = []
for tag in ways_tags:
    if len(tag) != 4:
        bad_tags.append(tag)
        print tag

        
print len(bad_tags)

# all tags have exactly 4 fields


# In[4]:

import csv
f = open('ways_tags_complete.csv', 'r')
ways_tags = csv.DictReader(f)

c = 0
for tag in ways_tags:
    c += 1
    
print c

