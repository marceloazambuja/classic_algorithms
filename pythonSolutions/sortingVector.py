myArray = [30, 12, 40, 8, 50, 5]

myArray.sort()

print ("Sorted array: ")

print myArray

myArray.sort(reverse = True)

print "Sorted descendent array: "

print myArray

print ("============= Ordering arrays with sublists:")

secondArray = [(16,18), (14,15), (12,13), (8, 10), (13,1)]


def orderFirst(val):
    return(val[0])

secondArray.sort(key=orderFirst)
print secondArray


def orderSecond(val):
    return(val[1])

print ("============= Ordering arrays with sublists by second value of sublist:")
secondArray.sort(key=orderSecond)
print secondArray

print ("============= Ordering arrays with sublists by second value of sublist in descending order:")
secondArray.sort(key=orderSecond, reverse=True)
print secondArray
