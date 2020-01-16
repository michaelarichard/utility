#!/usr/bin/env python

import sys
import yaml
import json

my_file='some_service1.yaml'


with open(r'E:\data\fruits.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    data = yaml.load(file, Loader=yaml.FullLoader)


print(yaml.dump(json.loads(data), default_flow_style=False))

print(json.dumps(y, indent=4))




