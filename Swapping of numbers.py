#SWAPPING OF TWO NUMBERS WITHOUT USING TEMPORARY VARIABLE
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
a=a+b
b=a-b
a=a-b
print("After swapping A value is : ",a)
print("After swapping B value is : ",b)
