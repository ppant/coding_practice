# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:54:19 2021

@author: pp
"""

# Sample json read operation
import json

# Opening JSON file
f = open('data.json')

# returns JSON object as a dict
data = json.load(f)

# Iterating through the json list
for i in data['glossary']:
    print(i)

# Close the file
f.close()
