mileage=float(input("Enter the Fuel Economy of your car:"))
distance=int(input("Enter the distance you want to travel:"))
price=float(input("Enter the fuel price in your area:"))

petrolrequired=distance/mileage
totalcost=(petrolrequired)*price

print("Total cost of your travel is:",totalcost)
print("Total petrol required to travel is:",petrolrequired,"litres")
