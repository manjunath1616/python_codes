#wap to perform the withdraw operation of an account..
#SEQUENCE FLOW OF EXECUTIONS:
'''acc_no=eval(input("Acccount number: "))
balance=eval(input("Initial balance:"))
print("*"*30)
print(f"{acc_no=}\n{balance=}")
print("*"*30)
with_draw=eval(input("Enter a withdraw amount:"))
print(f"please collect your withdraw amount:{with_draw}")
balance=balance-with_draw
print(f"After withdraw operation Balance in the account: {balance}")
print("Thank you for visiting")
# IF THE AMOUNT IS GREATER THEN INTIAL AMOUNT ......
# this code is worst'''

#IF CONDITIONS:
"""
acc_no=eval(input("Acccount number: "))
balance=eval(input("Initial balance:"))
print("*"*30)
print(f"{acc_no=}\n{balance=}")
print("*"*30)
with_draw=eval(input("Enter a withdraw amount:"))
if balance>=with_draw:
    print(f"please collect your withdraw amount:{with_draw}")
    balance=balance-with_draw
    print(f"After withdraw operation Balance in the account: {balance}")
print("Thank you for visiting")
"""

#IF-ELSE
'''
acc_no=eval(input("Acccount number: "))
balance=eval(input("Initial balance:"))
print("*"*30)
print(f"{acc_no=}\n{balance=}")
print("*"*30)
with_draw=eval(input("Enter a withdraw amount:"))
if balance>=with_draw:
    print(f"please collect your withdraw amount:{with_draw}")
    balance=balance-with_draw
    print(f"After withdraw operation Balance in the account: {balance}")
else:
    print("Transaction is declined:")
    print("Insufficent withdraw amount:")
print("Thank you for visiting")
'''
# another example for if condtions:
#wap for a leap year the condition is it is divisible by 4 and it is not divisible by 100
# or it is divisible by 400
year=eval(input("Enter a year : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year.........")
else:
    print(f"{year} is not leap year.......")




"""
#another example for IF-ELSE
xyz=eval(input("Enter a Number:"))
if xyz%2==0:
    print(f"{xyz} is even_number")
else:
    print(f"{xyz} is odd_number")
"""