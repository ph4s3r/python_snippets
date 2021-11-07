"""

This module reads config files and parses them into a dictionary

"""

from pathlib import Path


def testforPath(configfile_location: Path = None) -> Path:

    if configfile_location is not None:
        if not configfile_location.exists():
            print(f"config file at location {configfile_location} does not exist. "
                  f"Hit y if you want to provide new location or anything else to exit")
            answer = input("> ")
            if answer == 'y':
                print("Provide the new path please: \n")
                configfile_location = input("> ").upper().strip()
                configfile_location = testforPath(Path(configfile_location))
                return configfile_location
            else:
                print("Adios!")
                exit(0)

        else:
            return configfile_location
    else:
        print(f"Please provide the config file location")
        configfile_location = input("> ").upper().strip()
        return testforPath(Path(configfile_location))


def parseConfig(path: Path, separator: str = '=') -> dict:

    """ Reading the config file and putting every key and value to a dict """

    confdict = dict()

    with open(path, 'rt') as cfgfile:
        config = cfgfile.readlines()
        for celem in config:
            k, v = celem.strip().split(separator)
            confdict[k.strip()] = v

    return confdict

def retrieveConfigItemValuebyInput(confdict: dict) -> str:

    print(f"Listing the configs:")
    for item, value in confdict.items():
        print(item, value)
    while True:
        print("Please enter the config key you are looking for")
        key = input("> ").upper().strip()
        if key == 'exit':
            print("Adios!")
            exit(0)
        if key in confdict.keys():
            print(confdict[key])
            break
        else:
            print("Not found, you can try again or type exit to exit")

def retrieveConfigItemValuebyParam(confdict: dict, itemToSearch: str) -> str:

    try:
        return confdict[itemToSearch]
    except KeyError:
        print("Config key not found")
        return None


if __name__ == '__main__':

    c = testforPath(Path('config1.cfg'))
    d = parseConfig(c)
    # retrieveConfigItemValuebyInput(d)
    print(retrieveConfigItemValuebyParam(d, 'everything'))

