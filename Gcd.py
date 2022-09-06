def GCD(r,s):
    a=r%s
    if(a==0):
        return s
    else:
        return GCD(s,a)
c= int(input("Enter the first number :"))
d= int(input("Enter the second number :"))
print("The GCD of two numbers is:", GCD(c,d))
