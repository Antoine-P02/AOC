

def naive(source):
    file = open(source, "r")
    rawData = file.readlines()

    data = rawData[0].split(",")

    ranges = []
    res = 0

    for d in data:
        start, end = d.split("-")
        ranges.append((int(start), int(end)))

    for (s, e) in ranges:
        for x in range(s, e+1, 1):

            char = str(x)
            if (len(char) % 2 == 0):

                db_start = 0
                db_mid =  int(len(char)/2)
                db_stop = len(char)

                if ( char[db_start:db_mid] == char[db_mid:db_stop] ):
                    #print(x)
                    res += x

    return res


print(naive("2025/input2"))
print("--------------------------------")



def naive2(source):
    file = open(source, "r")
    rawData = file.readlines()

    data = rawData[0].split(",")

    ranges = []
    res = 0

    for d in data:
        start, end = d.split("-")
        ranges.append((int(start), int(end)))

    for (s, e) in ranges:
        for x in range(s, e+1, 1):

            char = str(x)

            #edge case all same number
            if (len(char) > 1) and char == ( char[0] * len(char)):
                res += x
            else:
                midPoint = len(char)//2

                for y in range(0, midPoint, 1):
                    segment = char[0:2+y]
                    offset1 = 2+y
                    offset2 = offset1 + len(segment)

                    while ( segment == char[offset1:offset2] and (offset2 <= len(char) ) ):
                        if ( offset2 == len(char) ):
                            res += x
                        offset1 += len(segment)
                        offset2 += len(segment)
    return res


print(naive2("2025/input2"))
print("Slight issue on duplicates, but works when result list is converted to set")
print("--------------------------------")

#45445300760 too high--
#45445300715 too high--
