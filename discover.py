#!/usr/bin/env python

import sys
import json
from bof.layers.knx import search

devices = []
knxDevices = search()
for knxDevice in knxDevices:
  device = {
    "name": knxDevice.name.replace("\u0000", ""),
    "ip_address": knxDevice.ip_address,
    "port": knxDevice.port,
    "knx_address": knxDevice.knx_address,
    "mac_address": knxDevice.mac_address,
    "multicast_address": knxDevice.multicast_address,
    "serial_number": knxDevice.serial_number
  }
  devices.append(device)

print(json.dumps(devices, indent=2))

