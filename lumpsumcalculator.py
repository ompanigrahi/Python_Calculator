initial= int(input("Enter the initail investment amount:"))
roi=float(input("Enter the Rate of Intrest:"))
time=int(input("Enter the time of investment(in years):"))
a=initial
month=time*12
print(month)
for i in range(time):
    a=a+(a*(roi/100))


print("Your investment is now worth:",int(a))
print("You invested rupees",initial )
print("The total gain in rupees is:", int(a-initial))
