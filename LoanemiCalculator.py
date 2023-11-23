#EMI = (P X R/12) X [(1+R/12) ^N] / [(1+R/12) ^N-1].
#EMI = [P x R x (1+R)^N]/[(1+R)^N-1]
principal=int(input("Enter the principal Amount:"))
rate=float(input("Enter the Rate Of Intrest:"))
term=int(input("Enter the term of the Loan"))
# EMI=(principal*(rate/12))*(((1+(rate/12))**term)/((1+(rate/12))**(term-1)))
EMI = (principal * rate * (1+rate)**term)/((1+rate)**term-1)

print("Your Emi will be:",EMI)