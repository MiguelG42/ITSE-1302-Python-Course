first_name = input("Enter you first name: ")
last_name = input("Enter your last name: ")

print()

current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print()

print("Hello, " + first_name + " " + last_name + "!\nYou are " + str(age) + " years old this year.")

age += 1

print ()

print(f"Next year, you will be {age} years old in {current_year + 1}.")

print()

print("Completed by, Miguel Gomez")
