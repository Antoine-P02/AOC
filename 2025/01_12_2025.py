

def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    start = 50
    count = 0

    for l in lines:

        sign, val = l[0], int(l[1:])

        if sign  == 'L':
            start = compute(start, -(val) )
        else:
            start = compute (start, val)

        if start == 0:
            count += 1
            
    return count


def compute(value, bonus):
    return (value + bonus) % 100


print(naive("2025/input1"))
print("--------------------------------")


def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    start = 50
    count = 0

    for l in lines:

        sign, val = l[0], int(l[1:])

        if sign  == 'L':
            if ( (start - val < 0 ) and (start != 0) ):
                print("L", val)
                count +=1
            start = compute2(start, -(val) )
        else:
            if start + val > 99:
                print("R", val)
                count += int ( (start+val) / 99 )
            start = compute2 (start, val)

        #print(start, "->", count)
        
        
            
    return count, naive(source)


def compute2(value, bonus):
    return (value + bonus) % 100


#print(naive2("2025/input12"))

def manual(source):
    file = open(source, "r")
    lines = file.readlines()

    start = 50
    count = 0

    for l in lines:

        sign, val = l[0], int(l[1:])

        if sign  == 'L':
            if val > start:
                val += 100
            start = start - val
        

        else:

        if start == 0:
            count += 1




print(manual("2025/input12"))

#1.5 -> 5012 too low
#1.5 -> 5615 too low

#1.5 -> 6518 too high 