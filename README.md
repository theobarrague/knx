# knx

![](https://img.shields.io/badge/License-MIT-blue)
![](https://img.shields.io/badge/Python-3.6.13-yellow)
![](https://img.shields.io/badge/BOF-1.0.1-orange)

University research project on the study of vulnerabilities around the KNX protocol.

## Getting started

I use [my fork](https://github.com/theobarrague/bof) of [BOF](https://github.com/Orange-Cyberdefense/bof) ( Boiboite Opener Framework ) from [Orange Cyberdefense](https://github.com/Orange-Cyberdefense) because I fixed some bugs and added some features which are not yet present in the initial project. You should do the same.

I also use [Python 3.6.13](https://www.python.org) from [pyenv 2.0.3](https://github.com/pyenv/pyenv) on a [Ubuntu 21.04](https://ubuntu.com) virtual machine running on [Hyper-V](https://en.wikipedia.org/wiki/Hyper-V).

According to my setup, you should start with something like that : 

```
pyenv install 3.6.13
pyenv global 3.6.13
python -m venv knx
cd knx
source bin/activate
git clone git@github.com:theobarrague/knx.git
git clone git@github.com:theobarrague/bof.git
ln -s $(pwd)/bof/bof $(pwd)/knx/bof
cd knx
```

## Usage

You will find several python scripts in this repository. Each script allows you to manipulate part of the protocol to carry out an attack.

When a script return informations, they are formatted in JSON to facilitate interconnection with other programs.

### `discover.py`

Allows you to discover KNX gateways on the local network.

```
knx@knx-vm:~/knx$ python discover.py 2>/dev/null
[
  {
    "name": "IP/KNX router TH210",
    "ip_address": "192.168.1.240",
    "port": 3671,
    "knx_address": "1.1.0",
    "mac_address": "00:0e:8c:01:0d:15",
    "multicast_address": "224.0.23.12",
    "serial_number": 4298526517
  }
]
```

### `write.py`

Allows you to send arbitrary data to a group address. You can use this script to turn on or off something for example.

```
knx@knx-vm:~/knx$ python write.py 192.168.1.240 0/0/1 1
```

### `sniff.py`

Allows you to sniff the KNX network to find out what is happening on it.

```
knx@knx-vm:~/knx$ python sniff.py 2>/dev/null
{
  "timestamp": 1627146126,
  "source": "1.1.255",
  "destination": "0.0.1",
  "type": "write",
  "data": 1
}
{
  "timestamp": 1627146128,
  "source": "1.1.255",
  "destination": "0.0.1",
  "type": "write",
  "data": 0
}
```


## Roadmap

* Write these scripts :
  * Restart KNX device
  * Keep a KNX device in a forced state ( on / off )
  * Obtain informations from KNX devices ( can be also used to ping )
  * <s>Sniff a KNX network</s>
  * <s>Send data to KNX devices</s>
  * <s>Discover KNX gateways on local network</s>
* Refactor all scripts according to Python standards
* Write a script to detect vulnerable KNX networks and identify their weaknesses

## Contribution

Pull requests are welcome.
