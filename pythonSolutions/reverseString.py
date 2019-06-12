# all codes here I copy from https://stackoverflow.com/questions/931092/reverse-a-string-in-python
# Developer might expect something like string.reverse(), but there is no built in reverse function for Python's str object. 
# In Python, strings are immutable. 
# Changing a string does not modify the string. It creates a new one. 
# But strings are sliceable. 
# Slicing a string gives you a new string from one point in the string, backwards or forwards, to another point, by given increments.

## Easiest form:
mystring  =   'my normal string'[::-1]
print (mystring)

## or even
print ('my normal string'[::-1])
# and    
print ('my normal string'[-1::-1])  #start:end:step (or start:end:stride)

################################################################
#### now a lot of tests to understand how string slicing works:
print ('coup_ate_grouping'[0])  ## => 'c'
print ('coup_ate_grouping'[1])  ## => 'o' 
print ('coup_ate_grouping'[2])  ## => 'u' 

## start (with negative integers)
print ('coup_ate_grouping'[-1])  ## => 'g'
print ('coup_ate_grouping'[-2])  ## => 'n' 
print ('coup_ate_grouping'[-3])  ## => 'i' 

## start:end 
print ('coup_ate_grouping'[0:4])    ## => 'coup'    
print ('coup_ate_grouping'[4:8])    ## => '_ate'    
print ('coup_ate_grouping'[8:12])   ## => '_gro'    

## start:end 
print ('coup_ate_grouping'[-4:])    ## => 'ping' (counter-intuitive)
print ('coup_ate_grouping'[-4:-1])  ## => 'pin'
print ('coup_ate_grouping'[-4:-2])  ## => 'pi'
print ('coup_ate_grouping'[-4:-3])  ## => 'p'
print ('coup_ate_grouping'[-4:-4])  ## => ''
print ('coup_ate_grouping'[0:-1])   ## => 'coup_ate_groupin'
print ('coup_ate_grouping'[0:])     ## => 'coup_ate_grouping' (counter-intuitive)

## start:end:step (or start:end:stride)
print ('coup_ate_grouping'[-1::1])  ## => 'g'   
print ('coup_ate_grouping'[-1::-1]) ## => 'gnipuorg_eta_puoc'

## combinations
print ('coup_ate_grouping'[-1::-1][-4:]) ## => 'puoc'


######## of course we can do something more 'normal'  like this:
variable = "string"
message = ""
for b in variable:
    message = b+message
print (message)

###### and, finally:
for char in reversed( variable ):  
  print( char, end = "" )  #the strange (end = "") is the python 3 way of not newlining at the end of each print. In python 2.x, you could just write print( char, )

print ("\n\n ")

######## final test
myString = ""
myString = input ('Enter your string: ')
print (myString[::-1])