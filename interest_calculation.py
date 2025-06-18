investment = int(input("Enter your monthly investment amount (less than $50,000): "))
while investment <= 0 or investment >= 50000:
    print("Invalid amount. Please enter a value greater than 0 and less than 50,000.")
    investment = int(input("Enter your monthly investment amount (less than $50,000): "))

rate = int(input("Enter annual interest rate (as a whole number less than 15%): "))
while rate <= 0 or rate >= 15:
    print("Invalid rate. Please enter a value greater than 0 and less than 15.")
    rate = int(input("Enter annual interest rate (as a whole number less than 15%): "))

years = int(input("Enter investment duration in years: "))
while years <= 0:
    print("Invalid duration. Please enter a number greater than 0.")
    years = int(input("Enter investment duration in years: "))

months = years * 12
monthly_rate = rate / 12 / 100
total = 0

for month in range(1, months + 1):
    total += investment
    interest = round(total * monthly_rate, 2)
    total += interest
    if month % 12 == 0:
        print(f"Year {month // 12}: Investment value = ${round(total, 2)}")

print()
print("Final Investment Summary")
print("Years Invested: " + str(years))
print("Yearly Interest Rate: " + str(rate) + "%")
print("Monthly Investment: $" + str(investment))
print("Total Value After Compounding: $" + str(round(total, 2)))
print()
print("Completed by, Miguel Gomez")
