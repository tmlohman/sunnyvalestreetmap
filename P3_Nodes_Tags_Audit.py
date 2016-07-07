
# coding: utf-8

# Auditing Nodes Tags file:
# - Id should be an integer, and should be in Nodes file
# - Each tag should have exactly 4 fields

# In[2]:

import os
os.getcwd()


# In[7]:

import csv
f = open('nodes_tags_complete.csv', 'r')
nodes_tags = csv.DictReader(f)
f2 = open('nodes_complete.csv', 'r')
nodes = csv.DictReader(f2)

known_nodes = set()
for node in nodes:
    known_nodes.add(node['id'])
    
known_nodes = sorted(known_nodes)

f = open('nodes_tags_complete.csv', 'r')
nodes_tags = csv.DictReader(f)

for tag in nodes_tags:
    t = tag['id']
    if t not in known_nodes:
        print tag
        
# All tags are in known_nodes, since all nodes are integers, this check is also satisfied.


# In[5]:

import csv
f = open('nodes_tags_complete.csv', 'r')
nodes_tags = csv.DictReader(f)

bad_tags = []
for tag in nodes_tags:
    if len(tag) != 4:
        bad_tags.append(tag)
        print tag

        
print len(bad_tags)


# In[ ]:



