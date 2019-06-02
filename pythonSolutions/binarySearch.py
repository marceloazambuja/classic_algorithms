def binarySearch(arr, leftPosition, rightPosition, target):
    #after some iterations without to find the target, righPosition can reach the very beggining of array.
    if rightPosition>0:
        #not so easy way to calculate de middle of each array portion
        middle=int(leftPosition + (rightPosition-leftPosition)/2)

        if arr[middle]==target:
            return middle
        elif arr[middle] > target: #the magic of recursively 
            return binarySearch(arr, leftPosition, middle-1, target)
        else:
            return binarySearch(arr, middle+1, rightPosition, target)

    else:
        return -1

# main program
values = [4, 8, 12, 15, 18, 20, 23]

lastIndex = len(values)-1  #to find the value of last index of array

find = int (input ("Searched Value: "))

position = binarySearch(values, 0, lastIndex, find)

if position!=-1:
    print ("Value found at position %d" % position)
else:
    print ("Value not exist in array")
    