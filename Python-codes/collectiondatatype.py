#list::: dynamic input list
#wap to read the list of values from the user & create the list object with those values::
'''
x=eval(input("Enter a list of values and it must be b/w []: "))
print("data type of x:  ",type(x))
'''
#append{adding the new element}
"""
manju=[12,43,'manju',True,False,'bhavya']
id(manju)       #addressing 
2086567503104   #ADREES OF MANJU.
manju.append('frds')   #INSERTION IN MANJU LIST
manju
[12, 43, 'manju', True, False, 'bhavya', 'frds']
id(manju)
2086567503104

#after inserting,deleting aslo the address of manju won"t be change.
"""
#deleting :  adressing:   append:  
""" 
>>> vals=[23,34,56,56]
>>> vals
[23, 34, 56, 56]
>>> id(vals)
2464429794560
>>> vals.append("manju")
>>> vals
[23, 34, 56, 56, 'manju']
>>> vals.append("5")
>>> vals
[23, 34, 56, 56, 'manju', '5']
>>> vals.append(5)
>>> vals
[23, 34, 56, 56, 'manju', '5', 5]
>>> del vals[0]
>>> vals
[34, 56, 56, 'manju', '5', 5]
>>>
"""
#len(vals) -----> TO FIND LENGTH OF THE LIST.


#TUPLE:
'''
>>> x=(23,24,45,'manju',True,4+8j,'manju',23)
>>> x
(23, 24, 45, 'manju', True, (4+8j), 'manju', 23)
>>> type(x)
<class 'tuple'>
>>> x[0]
23
>>> x[1:4]
(24, 45, 'manju')
'''
#insertion is not allowed:
"""
>>> x.append(45)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
"""
"""
>>> x=23,24,45,'manju',True,4+8j,'manju',233
>>> type(x)
<class 'tuple'>
"""
'''
 a=10
>>> type(a)
<class 'int'>
>>> b=(10)
>>> b
10
>>> type(b)
<class 'int'>
>>> ba=(10,)
>>> type(ba)
<class 'tuple'>
'''

#SET DATA TYPE::
"""
>>> x={23,34,23,23,345,"manju"}
>>> type(x)
<class 'set'>
>>> x
{345, 34, 23, 'manju'}
"""
"""
>>> x="THIS IS A MANJUNATH"
>>> txt=set(x)
>>> type(x)
<class 'str'>
>>> txt
{'H', ' ', 'M', 'U', 'T', 'J', 'N', 'A', 'S', 'I'}
>>> type(txt)
<class 'set'>
"""
#RANGE:
'''
manju=list(range(1,10,1))
>>> manju
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> ODDS=tuple(range(1,25,2))
>>> ODDS
(1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23)

>>> odds=set(range(1,10,4))
>>> odds
{1, 5, 9}

EVENS=tuple(range(2,25,2))
>>> EVENS
(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24)

>>> X=set(range(15))
>>> X
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
'''

#DICTIONARY DATA TYPE:
"""
>>> d1={"python":1000,2000:"manju","java":300}
>>> d1
{'python': 1000, 2000: 'manju', 'java': 300}
>>> type(d1)
<class 'dict'>
>>> d1[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> len(d1)
3
>>> d1["manju"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'manju'
>>> d1[2000]
'manju'
>>> d1["java"]
300
>>> d1["cpp"]=66.00000
>>> d1
{'python': 1000, 2000: 'manju', 'java': 300, 'cpp': 66.0}
>>> d1["python"]=100000
>>> d1
{'python': 100000, 2000: 'manju', 'java': 300, 'cpp': 66.0}
>>> d1["data"]=300
>>> d1
{'python': 100000, 2000: 'manju', 'java': 300, 'cpp': 66.0, 'data': 300}
"""
