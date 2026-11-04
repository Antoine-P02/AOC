

def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    res = 0

    for line in lines:

        tmp = []
        maxVal = 0

        data = [int(l) for l in line.strip()]
        firstData = data[0:len(data)-1]

        maxVal = max(firstData)

        while (max(firstData) == maxVal ):
            firstIndex = data.index(maxVal)

            remainderList = data[firstIndex+1:len(data)]
            fuse = int(str(maxVal) + str( max(remainderList) ) )
  
            tmp.append( fuse )
            firstData.remove(maxVal)

        res += max(tmp)
    return res

print(naive("2025/input3"))
print("--------------------------------")



def naive2(source, maxlen):
    file = open(source, "r")
    lines = file.readlines()

    res = 0

    for line in lines:

        tmp = []
        remainder = [int(l) for l in line.strip()]

        while (len(tmp) < maxlen):
            tmp, remainder = getBestInList(tmp, remainder, maxlen)

        final = ''.join(map(str, tmp))
        res += int(final)

        print(line.strip(), final)

    return res

def getBestInList(curr, remainder, maxlen):

    if ( len(curr) + len(remainder) == maxlen):
        curr += remainder
        return curr, remainder

    bestValueIndex = remainder.index(max(remainder))
    checkLen = len(curr) + (len(remainder) - bestValueIndex)

    if (checkLen >= maxlen):
        curr.append(max(remainder))
        remainder = remainder[bestValueIndex+1 : len(remainder)]
        return curr, remainder
    
    remainderCopy = remainder.copy()
    while checkLen < maxlen:

        remainderCopy.remove(max(remainderCopy))
        newMax = max(remainderCopy)
        bestValueIndex = remainder.index(newMax)
        checkLen = len(curr) + (len(remainder) - bestValueIndex)
        
    curr.append(newMax)
    remainder.remove(newMax)
    remainder = remainder[bestValueIndex : len(remainder)]

    return curr, remainder

        


print(naive2("2025/input3", 12) == 171388730430281)
print("--------------------------------")

#172044405405070 too high
#172029082599837 too high
# 171388730430281 valid