# Python key->value data structure is named Dictionary. Basically, a Dictionary is a list of unique key that has a pointed value. 
# Dictionary is a very good option for structures where we need search values based on their keys.
# Created by Marcelo Cunha de Azambuja on 6/9/19, based on https://www.geeksforgeeks.org/python-dictionary/

# Creating an empty Dictionary whithout use of built-in dict() function
Dict = {} #curly {} braces indicates that Dict is a Dictionary structure

print("Empty Dictionary: ") 
print(Dict) 
  
# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Adding set of values  
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
  
# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 
  
# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 

# accessing a element using key 
print("Acessing a element using key:") 
print(Dict[2]) 
  
# accessing a element using get() 
# method 
print("Acessing a element using get:") 
print(Dict.get(3)) 

# Deleting a Key  
# using pop() 
Dict.pop(3) 
print("\nPopping specific element: ") 
print(Dict) 

# Deleting a Key 
# using popitem() 
Dict.popitem() 
print("\nPops element with popitem will remove the newest element, the top of the stack: ") 
print(Dict)  