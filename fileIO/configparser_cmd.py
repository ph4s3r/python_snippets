#!/bin/python3

"""

This module retrieves a value from a config file

command line usage:

configparser_cmd.py <config_location> <config_key_to_retrieve>

"""

from pathlib import Path
import sys


def parseConfig(path: Path, separator: str = '=') -> dict:

    """ Reading the config file and putting every key and value to a dict """

    confdict = dict()

    with open(path, 'rt') as cfgfile:
        config = cfgfile.readlines()
        for celem in config:
            k, v = celem.strip().split(separator)
            confdict[k.strip()] = v

    return confdict

def retrieveConfigItemValuebyParam(confdict: dict, itemToSearch: str) -> str:

    try:
        return confdict[itemToSearch]
    except KeyError:
        print("Config key not found")
        return None

if __name__ == '__main__':

    if sys.argv[1] and sys.argv[2] is not None:
        d = parseConfig(Path(sys.argv[1]))
        print(retrieveConfigItemValuebyParam(d, sys.argv[2]))
    else:
        exit(255)

