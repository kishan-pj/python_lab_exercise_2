# Given three integer . print the smallest one.

a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=int(input("enter the values of c: "))
if a<b and b<c:
    print("The smallest number",a)
elif b<c and a<c:
    print("The smallest number",b)
else:
    print("The smallest number is",c)