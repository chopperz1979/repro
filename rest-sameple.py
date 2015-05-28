#!/usr/bin/python

import requests
import json

# put the ip address or dns of your apic-em controller in this url
url = 'https://sandboxapic.cisco.com/api/v0/host/1/3'
#url = 'https://sandboxapic.cisco.com/api/v0/link'
#url = 'https://sandboxapic.cisco.com/api/v0/network-device/cceaf2fe-c3d9-4d37-bf14-fba071c27d6e/config'

# this statement performs a GET on the specified url
try : 
    response = requests.get(url, verify=False)

    get_devices_json = response.json()

    #print (json.dumps(get_devices_json, indent=4, sort_keys=False))

    if get_devices_json['response'] : 
        #print get_devices_json['response']
        print (json.dumps(get_devices_json, indent=4, sort_keys=False))
    #else:
        #print (json.dumps(get_devices_json, indent=4, sort_keys=False))
except:
    print 'Error in getting the request from the APIC-EM'
