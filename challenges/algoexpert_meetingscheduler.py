
# https://www.youtube.com/watch?v=3Q_oYDQ2whs

# I only wrote the part to calculate free time, did not want to implement the freetime overlap calc

# Sample input:

tim_meetings = [
    ['9:00','10:30'],['12:00','13:00'],['16:00','18:00']
    ]
tim_boundaries = ['9:00','20:00']

mich_meetings = [
    ['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']
    ]
mich_boundaries = ['10:00','18:30']

#Sample output:

result = [
    ['11:30','12:00'],['15:00','16:00'],['18:00','18:30']
]

def convertToMins(time: str) -> int:
    # example input: '11:30'
    h,m = int(time.split(":"))

    return h*60 + m

def freetimebetween(meetings_end: str, next_meetings_beginning: str) -> list():
    """
        the input is two time strings, and the output is
            - None if there is no free time between the 2 meetings
            - The list of time-pair strings, basically a free slot, between them
    """

    # Assuming no overlapping meetings. When they overlap we need to substract or something

    if meetings_end != next_meetings_beginning:
        return [meetings_end, next_meetings_beginning]
    else:
        return None


def freeslotcalc(boundaries: list, meetings: list) -> list():

    #Run through the day from boundary to boundary through meetings, and gather free slots
    freeslots = list()

    daystart = freetimebetween(boundaries[0], meetings[0][0])

    if daystart is not None:
        freeslots.append(daystart)

    for i in range(len(meetings)-1):
        if freetimebetween(meetings[i][1], meetings[i+1][0]) is not None:
            freeslots.append(freetimebetween(meetings[i][1], meetings[i+1][0]))

    dayend = freetimebetween(meetings[i+1][1], boundaries[1])

    if dayend is not None:
        freeslots.append(dayend)

    return freeslots

def overlaps(person1_freeslots: list, person2_freeslots: list):
    """
    Example inputs:
    [['11:30', '12:30'], ['15:00', '16:00'], ['17:00', '18:30']]
    [['10:30', '12:00'], ['13:00', '16:00'], ['18:00', '20:00']]


    Calculates free meeting slots from 2 persons free time arrays
    Let`s just go through on list at first, and see if the other person is free anywhere between
    Like the first block to see is ['11:30', '12:30'] -> does the other person have time in there?
    Well, let`s pick the first free block of the other person and see
    """

    for slot1 in person1_freeslots:
        s1s = convertToMins(slot1[0])
        s1e = convertToMins(slot1[1])
        for slot2 in person2_freeslots:
            s2s = convertToMins(slot2[0])
            s2e = convertToMins(slot2[1])

            if s1s <= s2s <= s1e:
                print("there is a free slot")



    pass



mich_freetime = freeslotcalc(mich_boundaries, mich_meetings)
tim_freetime = freeslotcalc(tim_boundaries, tim_meetings)

print(mich_freetime)
print(tim_freetime)
