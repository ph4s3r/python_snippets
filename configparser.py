""" This module reads config files and parses them into a dictionary"""

from pathlib import Path


def testforPath(configfile_location: str):

    if not configfile_location.exists():
        print(f"config file at location {configfile_location} does not exist. "
              f"Hit y if you want to provide new location or anything else to exit")
        answer = input()
        if answer == 'y':
            print("Provide the new path please: \n")
            configfile_location = input()
            configfile_location = testforPath(Path(configfile_location))
            return configfile_location
        else:
            print("Adios!")
            exit(0)

    else:
        return configfile_location


def parseConfig(path: Path, separator: str = '=') -> None:

    """ Reading the config file and putting every key and value to a dict """

    confdict = dict()

    with open(path, 'rt') as cfgfile:
        config = cfgfile.readlines()
        for celem in config:
            k, v = celem.strip().split(separator)
            confdict[k.strip()] = v

    print(confdict)


if __name__ == '__main__':

    c = Path('config.cfg')
    c = testforPath(c)
    parseConfig(c)
