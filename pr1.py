
print("Welcome to the User Information Program!")
print("This program collects your basic details, processes them,")
print("and shows how Python handles different data types.\n")


name = input("Enter your name: ")

age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))
favourite_number = int(input("Enter your favourite number: "))


current_year = 2026
birth_year = current_year - age

print("\n--- Variable Details (Value | Type | Memory Address) ---")
print("Name:", name, "|", type(name), "|", id(name))
print("Age:", age, "|", type(age), "|", id(age))
print("Height:", height, "|", type(height), "|", id(height))
print("Favourite Number:", favourite_number, "|", type(favourite_number), "|", id(favourite_number))
print("Birth Year:", birth_year, "|", type(birth_year), "|", id(birth_year))


print("\n--- User Summary ---")
print(f"Hello {name}!")
print(f"You are {age} years old and approximately {height} meters tall.")
print(f"Your favourite number is {favourite_number}.")
print(f"You were likely born in {birth_year}.")

print("\n--- Data Type Conversions ---")
print("Age was converted from string to integer.")
print("Height was converted from string to float.")
print("Favourite number was converted from string to integer.")


print("\nThank you for using this program!")
print("Keep exploring Python — it’s powerful and fun 🚀")
