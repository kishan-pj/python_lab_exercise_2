# Write a python program to sum of three given integer. However,if two values are equal sum will be zero.

def sum(a,b,c):
    if a==b or b==c or c==a:
        sum=0;
    else:
        sum=(a+b+c)
    return sum
x,y,z=[int(a) for a in input ("enter three number: ")]
print(sum(x,y,z))
