# Check whether the given year is leap year or not.
# If year is leap print LEAP YEAR else print COMMON YEAR.

year=int(input("enter the number: "))
b= year%4
if b==0:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")

