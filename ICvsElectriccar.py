electriccar=int(input("Enter the ex showroom price of Electric car:"))
iccar=int(input("Enter the ex showroom price of IC car:"))
fueltype=input("Enetr the fuel type of the car:")
mileage=int(input("Enter the mileage of the IC car:"))
fuel=int(input("Enter the current fuel price"))
kmsdriving=int(input("Enter the number of KM's of driving per day:"))
insurance=0
registrationcost=0
onroad=0 
if fueltype in ("Diesel","diesel","DIESEL"):
    insurance=0.05*iccar
    registrationcost=.1*iccar
    onroad=insurance+registrationcost+iccar
    print(onroad)
if fueltype in ("Petrol","petrol","PETROL"):
    insurance=0.05*iccar
    registrationcost=0.06*iccar
    onroad=insurance+registrationcost+iccar

onroadelectic= 0.06*electriccar+electriccar
onroadpricediff=onroadelectic-onroad
print("In the initial phase, you will save",onroadpricediff,"on IC car over electric car")

runningcostelectric=kmsdriving*.3
runningcostic= (fuel/mileage)*kmsdriving

print("The per day running cost of Electric vehicle is:",runningcostelectric)
print("The per day running cost of IC car is:",runningcostic)
for i in range(2**100):
    if ((i*runningcostelectric)+electriccar)<((i*runningcostic)+iccar):
        print("Your money will be recovered in ",i,"days")
        print("Or",int(i/365),"years")
        break