#!/usr/bin/env python
from __future__ import print_function, unicode_literals 
import json 
from pprint import pprint 
import sys 

filename = "Instrumental_metrics.json"
#filepath = "instrumental_data.txt"
#sys.stdout = open(filepath,"w")
with open(filename) as f:
    json_data = json.load(f)
    pprint(json_data['response']['metrics'])
#    with open("instrumental_data.json","w") as json_file:
#       print(json_data,file=json_file)
#        json_file.close()
