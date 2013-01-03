#-*- coding: utf-8 -*-

import os, sys

### Get path of JSON file
if len(sys.argv) != 2:
  sys.exit("expected json file")

json_file_path = sys.argv[1]

### Parse and fix
import json, time

def fix_fields(data_part):
    old = data_part['AUTHORS']
    data_part['AUTHORS'] = data_part['AUTHORS'].replace(',', ', ').replace('  ', ' ')
    print 'authors_homogenization\n   [%s] [%s]' %(old, data_part['AUTHORS'])

    return data_part

json_file = open(json_file_path, 'r')
#json.load(json_data, object_hook = authors_homogenization)
new_data  = json.dumps(json.load(json_file, object_hook = fix_fields), sort_keys=True, indent=4)
json_file.close()

json_file = open(json_file_path, 'w')
json_file.write(new_data)
json_file.close()
