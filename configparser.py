from pathlib import Path
import os

def testforPath(configfile_location: str):

    if not configfile_location.exists():
        print(f"config file at location {configfile_location} does not exist. "
              f"Hit y if you want to provide new location or anything else to exit")
        answer = input()
        if answer == 'y':
            print("Provide the new path please: \n")
            configfile_location = input()
            configfile_location = testforPath(Path(configfile_location))
        else:
            print("Adios!")
            exit(0)

    else:
        return configfile_location



def parseConfig():
    with open(p: , 'rt') as cfgfile:
        for line in cfgfile.readline():
            print(line)


if __name__ == '__main__':

    c = Path('config1.cfg')
    c = testforPath(c)
    parseConfig(c)