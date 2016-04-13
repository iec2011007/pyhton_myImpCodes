#!/usr/bin/python
import json
import sys

jsonFilePath = sys.argv[1]

with open(jsonFilePath) as data_file:
	data = json.load(data_file)

jsonString = json.dumps(data)
print jsonString.replace(r'"', r'\"')
