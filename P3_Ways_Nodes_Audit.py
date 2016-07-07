
# coding: utf-8
Ways Nodes Audit
- All nodes should exist within the Nodes file
- All fields should be integers
* All ways should include at least 2 nodes
* Each node should have a unique and sequential position value
# In[3]:

# Completeness Audit - are all nodes within ways included in nodes data set?
# Repeat for complete data set
import csv
ways_nodes = csv.DictReader(open("ways_nodes_complete.csv"))

nodes = csv.DictReader(open("nodes_complete.csv"))

nodes_set = set() 
for node in nodes:
    nodes_set.add(int(node['id']))
print len(nodes_set)

# build a set of all the ways nodes
ways_nodes_set = set()
for node in ways_nodes:
    ways_nodes_set.add(int(node['node_id']))
    
# check if each node in the ways_nodes_set is in the nodes_set, make a list of ones that aren't
unknown_nodes = set()
for node in ways_nodes_set:
    if node not in nodes_set:
        unknown_nodes.add(node)
        
print len(ways_nodes_set)
print len(unknown_nodes)

print float(4960/400339)

# 4960 of 400,339 nodes are not accounted for in the nodes data set. This represents 1.2% of the overall data and 
# seems a small enough portion to overlook.


# In[2]:

# checking that all fields are integers

import csv
f = open("ways_nodes_complete.csv", 'r')
ways_nodes = csv.DictReader(f)

def check_type(data):
    try:
        int(data)
    except:
        print data
        
for node in ways_nodes:
    check_type(node['id'])
    check_type(node['node_id'])
    check_type(node['position'])
    
# all fields are integers


# In[3]:

import csv
f = open("ways_nodes_complete.csv", 'r')
ways_nodes = csv.DictReader(f)

c = 0
for node in ways_nodes:
    c += 1
    
print c


# In[ ]:

#checking node counts and sequence

import csv
f = open("ways_nodes_complete.csv", 'r')
ways_nodes = csv.DictReader(f)

ways = []
for node in ways_nodes:
    d = {node['node_id']:node['position']} #dictionary holdes node id and its position
    s = [] # empty list for dictionaries
    w = {node['id']:s} #dictionary for list of node postions
    if node['id'] not in ways_nodes:
        ways_nodes.append(w)
    if node['id'] in ways_nodes:
        ways_nodes.

