#This Calculator is based on fincalc blog stepup calculator
#Link :- https://fincalc-blog.in/step-up-sip-calculator-fincalc/

sip=int(input("Enter the Monthly SIP Amount:"))
intrest=float(input("Enter the Rate of Intrest:"))
year=int(input("Enter the number of Year:"))
stepup=int(input("Enter the stepup percent"))
month=year*12

a=0
for i in range(year):
    if i== 0:
        for j in range(12):
            intrestreceived=((a+sip)*(intrest/1200))
            a=intrestreceived+a+sip

    if i>0:
        sip=sip+(sip*stepup/100)
        for j in range(12):
            intrestreceived=((a+sip)*(intrest/1200))
            a=intrestreceived+a+sip

print(a)
z=a/100000
print(int(z),'lakhs')

ans=input("Do You want to run this program again:(yes/no)")
if ans in ('yes','YES','Yes'):
    sip=int(input("Enter the Monthly SIP Amount:"))
    intrest=float(input("Enter the Rate of Intrest:"))
    year=int(input("Enter the number of Year:"))
    stepup=int(input("Enter the stepup percent"))
    month=year*12

    a=0
    for i in range(year):
        if i==0:
            for j in range(12):
                intrestreceived=((a+sip)*(intrest/1200))
                a=intrestreceived+a+sip

        if i>0:
            sip=sip+(sip*stepup/100)
            for j in range(12):
                intrestreceived=((a+sip)*(intrest/1200))
                a=intrestreceived+a+sip
    print(a)


if ans in ('no','No','NO'):
    exit()
