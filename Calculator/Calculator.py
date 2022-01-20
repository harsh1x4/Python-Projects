x=int(input("Enter 1st Number : "))
y=int(input("Enter 2nd Number : "))
result=str(input("Enter What You Want TO Do With This(+,-,*,/,%(remainder),//(quotient)) : "))
add=x+y
mult=x*y
div=x/y
sub=x-y
quotient=x//y
remainder=x%y
if result=="+":
    print("This is The Addition : ",add)
elif result=="-":
    print("This Is The Subtraction : ",sub)
elif result=="*":
    print("This Is The Multiplication : ",mult)
elif result=="/":
    print("This Is The Divison : ",div)
elif result=="%":
    print("This is The Remainder : ",remainder)
elif result=="//":
    print("This is The Quotient : ",quotient)
else:
    print("Input Value is Wrong")

