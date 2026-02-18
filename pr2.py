

def star_pattern(n):
    print("\nStar Pattern:")
    for i in range(1, n + 1):
        print("*" * i)


def number_pattern(n):
    print("\nNumber Pattern:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()




def number_analyzer():
    try:
        num = int(input("\nEnter a number: "))

        
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

        
        if num > 0:
            print("Positive number")
        elif num < 0:
            print("Negative number")
        else:
            print("Zero")

        
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    print("Not a Prime number")
                    break
            else:
                print("Prime number")
        else:
            print("Not a Prime number")

    except ValueError:
        print("Invalid input! Please enter an integer.")




def sum_of_numbers():
    try:
        n = int(input("\nHow many numbers you want to add? "))
        total = 0

        for i in range(n):
            num = float(input(f"Enter number {i+1}: "))
            total += num

        print("Total sum =", total)

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def main():
    while True:
        print("\n========= LOGIC BOX MENU =========")
        print("1. Print Star Pattern")
        print("2. Print Number Pattern")
        print("3. Number Analyzer")
        print("4. Sum of N Numbers")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                n = int(input("Enter number of rows: "))
                star_pattern(n)
            except ValueError:
                print("Invalid input! Please enter an integer.")

        elif choice == '2':
            try:
                n = int(input("Enter number of rows: "))
                number_pattern(n)
            except ValueError:
                print("Invalid input! Please enter an integer.")

        elif choice == '3':
            number_analyzer()

        elif choice == '4':
            sum_of_numbers()

        elif choice == '5':
            print("Exiting program... Thank You!")
            break

        else:
            print("Invalid choice! Please select 1-5.")



if __name__ == "__main__":

    main()
