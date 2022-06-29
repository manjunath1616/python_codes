#wap for which number is biggest:
#[NESTED IF-ELSE]
'''
x=eval(input("Enter a value x:"))
y=eval(input("Enter a value y:"))
z=eval(input("Enter a value z:"))
if x>y and x>z:
    print(f"{x=} is biggest among three")
else:
    if y>z:
        print(f"{y=} is biggest")
    else:
        print(f"{z=} is biggest")
'''

# while condtions is more if-else statement is worst: provide bad lines of code
#BETTER WAY FOR MORE CONDITIONS IS "ELIF" STATEMENT:
#EX:
'''
code=eval(input("Enter a code between 1 and 5 :"))
if code==1:
    print("blue color")
elif code==2:
    print("yellow color")
elif code==3:
    print("black color")
elif code==4:
    print("white color")
elif code==5:
    print("Red color")
else:
    print("INVALID CODE...............")
'''

#31 days --- jan , mar, july, aug, oct, dec
#30 days---- apr, june, sep, nov
#28 days---- non leap year
#29 days ----leap year
"""
month=eval(input("Enter a number between range 1 to 12:"))
if month==1 or month==3 or month==7 or month==8 or month==10 or month==12:
    print("31 days in this month")
elif month==4 or month==6 or month==9 or month==11:
    print("30 days in this month")
elif month==2:
    year=eval(input("Enter a year:"))
    if (year%4==0 and year%100!=0) or (year%400==0):
              print(" 29 days in feb leep year")
    else:
        print("28 days not a leap year")
else:
    print("INVALID MONTH NUMBER")
    """
month=eval(input("Enter a number between range 1 to 12:"))
var_1=[1,3,7,8,10,12]
var_2=[4,6,9,11]
if month in var_1:
    print("31 days in this month")
elif month in var_2:
    print("30 days in this month")
elif month==2:
    year=eval(input("Enter a year:"))
    if (year%4==0 and year%100!=0) or (year%400==0):
              print(" 29 days in feb leep year")
    else:
        print("28 days not a leap year")
else:
    print("INVALID MONTH NUMBER")
