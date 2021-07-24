#!/usr/bin/env python

import json

from datetime import datetime
from bof.layers.raw_scapy import knx
from scapy.all import *

def i2repr(x):
    if x is None:
        return None
    else:
        return "%d.%d.%d" % ((x >> 12) & 0xf, (x >> 8) & 0xf,(x & 0xff))

def foo(packet):
    if "KNXnet/IP" not in packet:
        return

    if packet["KNXnet/IP"].service_identifier == 0x0530:
        cemi = packet["KNXnet/IP"]["ROUTING_INDICATION"].cemi
        # cemi.show2()

        source = i2repr(cemi.cemi_data.source_address)
        destination = i2repr(cemi.cemi_data.destination_address)
        acpi = cemi.cemi_data.acpi
        data = cemi.cemi_data.data

        if acpi == 2:
            acpi = "write"
        else:
            return

        request = {
            "timestamp": int(datetime.timestamp(datetime.now())),
            "source": source,
            "destination": destination,
            "type": acpi,
            "data": data
        }

        print(json.dumps(request, indent=2))

sniff(filter="udp and port 3671", prn=foo)
