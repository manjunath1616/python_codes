#conditional statment:
#2 biggest numbers
'''
x=eval(input("enter a value:"))
y=eval(input("Enter a value:"))
print(f"biggest={x if x>y else y}")
'''
'''
x=eval(input("enter a value:"))
y=eval(input("Enter a value:"))
if x>y:
    print(x)
else:
    print(y)
'''
'''
# wap wether the number is divisble by 100 or not
x=eval(input("Enter a value:"))
print(f"Given number {x} is divisible by 100" if x%100==0 else print("Given number {x} is not divisible by 100"
))
'''

#wap for 3 biggest numberes

from tkinter import Y


x=eval(input("Enter a value:"))
y=eval(input("Enter a value:"))
z=eval(input("Enter a value:"))
print(f"Biggest among three valuse:{x if y<x>z else y if y>z else z}")


