
# coding: utf-8

# Auditing Nodes File:
# - All nodes should be within the expected boundaries
# - Latitudes and longitudes should be floats
# - All nodes should be defined exactly once
# - Id, version, changeset, and uid should be integer values
# - Timestamp should be in standard format
# - All nodes should have exactly 8 fields
# - All timestamps should have occurred before the file was downloaded

# In[4]:

import os
os.getcwd()


# In[21]:

import csv
f = open('nodes_complete.csv', 'r')
nodes = csv.DictReader(f)


# In[10]:

# All nodes should be within expected boundaries, and all latitudes and longitudes can be represented as floats

def check_lat_lon(node):
    lat = float(node['lat'])
    lon = float(node['lon'])
    if 37.3375411 <= lat <= 37.416847 and -122.0624131 <= lon <= -121.986839:
        return None
    else:
        return node['id']
    
bad_nodes = []
for node in nodes:
    if check_lat_lon(node) != None:
        bad_nodes.append(check_lat_lon(node))
        
print len(bad_nodes)

# All nodes are within expected boundaries, and all latitudes and longitudes can be represented as floats


# In[22]:

# All nodes should be defined exactly once, and can be typed as integers

nodes_set = set()
repeated_nodes = {}

def check_nodes_set(node, nodes_set, repeated_nodes):
    n = int(node['id'])
    if n not in nodes_set:
        nodes_set.add(n)
    else:
        repeated_nodes[n] += 1
    return repeated_nodes
     
for node in nodes:
    check_nodes_set(node, nodes_set, repeated_nodes)

print len(nodes_set)
print len(repeated_nodes)

# There are 400,610 nodes, none are repeated, and all can be typed as integers


# In[ ]:




# In[1]:

# Version, changeset, and uid can all be typed as integers
import csv
f = open('nodes_complete.csv', 'r')
nodes = csv.DictReader(f)

def check_type(data):
    try:
        int(data)
    except:
        print data
        
for node in nodes:
    check_type(node['uid'])
    check_type(node['changeset'])
    check_type(node['version'])
    
# All uid, version, and changeset are the correct type
    


# In[36]:

# All nodes should have exactly 8 fields

import csv
f = open('nodes_complete.csv', 'r')
nodes = csv.DictReader(f)

for node in nodes:
    if len(node) != 8:
        print node
        
# All nodes have exactly 8 fields


# In[38]:

# Time and date should be in standard format
import re
import csv

f = open('nodes_complete.csv', 'r')
nodes = csv.DictReader(f)

date_time = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")

for node in nodes:
    try:
        date_time.match(node['timestamp'])
    except:
        print node['timestamp']
    
# All times and dates are in standard format


# In[7]:

# All timestamps should have occurred before the file was downloaded
import csv
f = open('nodes_complete.csv', 'r')
nodes = csv.DictReader(f)
download_date_time = "2016-06-17T15:49:00Z" # File was downloaded at 8:49AM PST on 6/17/16


for node in nodes:
    if node['timestamp'] >= download_date_time:
        print node['timestamp']

# All timestamps occured before download


# In[ ]:




# https://docs.python.org/2/library/re.html
# http://pythex.org/
# https://www.w3.org/TR/NOTE-datetime
