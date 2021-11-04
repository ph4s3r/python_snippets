#!/bin/python3

import string
import time


def genadditionalhashes(s):
    # function takes one password and generates all the hashes for possible appended characters
    asciidict = string.printable
    hashlist = [h(s)]
    for c in asciidict:
        hashlist.append(h(s + str(c)))

    return hashlist


def h(s):
    # hash function
    superhash = 0
    rev_iter = len(s) - 1
    for c in s:
        superhash = superhash + ord(c) * pow(131, rev_iter)
        rev_iter = rev_iter - 1

    return superhash % 1000000007


def authEvents(events):
    results = []
    passhashlist = []
    for i in events:
        if i[0] == "setPassword":
            #print("password changed to:", i[1])
            passhashlist = genadditionalhashes(i[1])
            #print("hashes generated for the above pass:", passhashlist)
        elif i[0] == "authorize":
            #print("authing:", i[1], "vs passhash:", passhash)
            if int(i[1]) in passhashlist:
                results.append("1")
            else:
                results.append("0")
    return results


if __name__ == '__main__':
    start_time = time.time()

    f = open("input2.txt", "r")
    n = int(f.readline())
    f.readline()

    events = []
    for line in f:
        events.append(line.rstrip().split())

    result = authEvents(events)
    print(result)
    f.close()
    print("--- %s msec ---" % round((time.time() - start_time)*1000,6))


