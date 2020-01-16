#!/usr/bin/env python

import sys
import yaml
import json
import base64
import os


def base64_encode(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return(base64_message)

def base64_decode(data):
    base64_message = data
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return(message)

my_key = os.getenv('SECRET_KEY')
my_value = os.getenv('SECRET_VALUE')

if os.getenv('SECRET_TEMPLATE'):
    my_template = os.getenv('SECRET_TEMPLATE')
else:
    my_template = 'samples/secret2.yaml'

with open(my_template,"r") as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    secret_template = yaml.load(file, Loader=yaml.FullLoader)

secret_template['data'] = {}
secret_template['data'][my_key] = base64_encode(my_value)


# my_file='samples/secret1.yaml'
# with open(my_file,"r") as file:
#     # The FullLoader parameter handles the conversion from YAML
#     # scalar values to Python the dictionary format
#     data = yaml.load(file, Loader=yaml.FullLoader)


#print(yaml.dump(data, default_flow_style=False))
print(yaml.dump(secret_template, default_flow_style=False))
#print(json.dumps(data, indent=4))

print("----------\n")

print("SECRET_USERNAME={}\n".format(os.getenv("SECRET_USERNAME")))
print("SECRET_TEMPLATE={}\n".format(os.getenv("SECRET_TEMPLATE")))

print("----------")

print("------Michael is awesome.-")

#print(base64_decode(data['data']['username']))
#print(base64_decode(data['data']['password']))

