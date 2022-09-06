#check whether it is a palindrome or not

a = input("Enter a string: ")
b = a[::-1]
if(a == b):
    print(a," is a palindrome")
else:
    print(a," is not a palindrome")
