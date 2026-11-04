

def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    ranges = []
    switch = False
    ingredients = []

    for line in lines:

        content = line.strip()
        
        if (not switch):
            if (content == ''):
                switch = True

            else:
                start, end = content.split("-")
                ranges.append( (int(start), int(end)) )
        else:
            ingredients.append(int(content))

    ranges.sort()

    count = 0
    total = 0

    for ingredient in ingredients:
        if (find(ranges, ingredient)):
            count += 1

        total += 1

    print(count, "/", total)
    return count

            
def find(ranges, item):
    start = 0
    end = len(ranges)

    for x in range( (len(ranges)//2) + 1 ):

        mid = (start + end) // 2

        if ( ranges[mid][0] <= item <= ranges[mid][1] ):
            #print("Found", item, "in", ranges[mid])
            return True

        if ( item < ranges[mid][0] ):
            #print("Item", item, "is less than", ranges[mid], "at index", x, "      ", start, mid, end)
            end = mid
            start = 0
            
        if ( item > ranges[mid][1] ):
            #print("Item", item, "is greater than", ranges[mid], "at index", x, "      ", start, mid, end)
            start = mid
            
    return False




print(naive("2025/input5"))
print("--------------------------------")




def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    ranges = set()

    for line in lines:

        print(line)

        content = line.strip()

        if (content == ''):
            return len(ranges)
        
        start, end = content.split("-")
        start = int(start)
        end = int(end)


        for x in range(start, end+1):
            ranges.add(x)

def optimizedPart2(source):
    file = open(source, "r")
    lines = file.readlines()

    ranges = []
    switch = False
    ingredients = []

    for line in lines:

        content = line.strip()
        
        if (not switch):
            if (content == ''):
                switch = True

            else:
                start, end = content.split("-")
                ranges.append( (int(start), int(end)) )
        else:
            ingredients.append(int(content))

    ranges.sort()

    for x in range(len(ranges)-1):
        curr = ranges[x]
        nextR = ranges[x+1]

        if (curr[1] >= nextR[0]  ):
            curr = (curr[0], max(curr[1], nextR[1]))
            ranges[x] = ( curr[0], max(curr[1], nextR[1]) )
            ranges.pop(x+1)
            ranges.insert(0, (0, 0))

    count = 0

    for (start, end) in ranges:
        if (start, end) != (0, 0):
            count += (end - start)+1

    return count






print(optimizedPart2("2025/input5"))
print("--------------------------------")

#681 too low