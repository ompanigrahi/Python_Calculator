
initial=int(input("Enter the Initial Amount Of Investment:"))
sip=int(input("Enter the Monthly SIP Amount:"))
intrest=float(input("Enter the Rate of Intrest:"))
year=int(input("Enter the number of Year:"))
month=year*12

a=float(initial+(initial*(intrest/1200)))
for i in range(month):
    intrestreceived=((a+sip)*(intrest/1200))
    a=intrestreceived+a+sip

print(a)

ans=input("Do You want to run this program again:(yes/no)")
if ans==('yes','YES','Yes'):
    initial=int(input("Enter the Initial Amount Of Investment:"))
    sip=int(input("Enter the Monthly SIP Amount:"))
    intrest=float(input("Enter the Rate of Intrest:"))
    month=int(input("Enter the number of Month:"))

    a=float(initial+(initial*(intrest/1200)))
    for i in range(month):
        intrestreceived=((a+sip)*(intrest/1200))
        a=intrestreceived+a+sip

    print(a)


if ans==('no','No','NO'):
    exit()
