n=int(input("enter the year:"))
if n%4==0 and n%400!=0 or n%100==0:
    print("enter the year is  leap",n)
else:
    print("enter the year is not leap ",n)
