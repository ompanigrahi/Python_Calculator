initial = 1
target = 10000000  # Target amount (1 crore)

while True:
    sip = int(input("Enter the Monthly SIP Amount: "))
    interest = float(input("Enter the Rate of Interest (per year in %): "))
    
    a = float(initial)
    month = 0

    # Loop until the target amount is reached
    while a < target:
        interest_received = ((a + sip) * (interest / 1200))
        a += interest_received + sip
        month += 1

    years = month // 12
    remaining_months = month % 12

    print(f"\nYou will reach ₹{target:,} in approximately {years} years and {remaining_months} months.\n")
    
    ans = input("Do you want to run this program again? (yes/no): ").strip().lower()
    if ans not in ['yes', 'y']:
        print("Program exited.")
        break
