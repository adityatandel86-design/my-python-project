

dataset = []
dataset_summary = {}


def input_data():
    """Function to input 1D or 2D data from the user"""
    global dataset

    print("\n1. Enter 1D List")
    print("2. Enter 2D List")
    choice = int(input("Enter choice: "))

    if choice == 1:
        data = list(map(int, input("Enter numbers separated by space: ").split()))
        dataset = data

    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        dataset = []

        for i in range(rows):
            row = list(map(int, input(f"Enter row {i+1} values: ").split()))
            dataset.append(row)

    print("Data stored successfully!\n")



def display_summary():
    """Displays dataset statistics using built-in functions"""
    global dataset_summary

    if not dataset:
        print("Dataset empty")
        return

    if isinstance(dataset[0], list):
        flat = [item for row in dataset for item in row]
    else:
        flat = dataset

    total = len(flat)
    minimum = min(flat)
    maximum = max(flat)
    total_sum = sum(flat)
    avg = total_sum / total

    dataset_summary = {"Total": total, "Min": minimum, "Max": maximum, "Average": avg}

    print("\nData Summary")
    print("Total elements:", total)
    print("Minimum value:", minimum)
    print("Maximum value:", maximum)
    print("Sum:", total_sum)
    print("Average:", round(avg,2))



def find_duplicates(data):
    """Find duplicate values in dataset"""
    seen = set()
    duplicates = set()

    for num in data:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

def show_values(*args):
    """Displays multiple values using *args"""
    print("\nValues received:")
    for val in args:
        print(val)



def dataset_info(**kwargs):
    """Displays dataset information using **kwargs"""
    print("\nDataset Info")
    for key,value in kwargs.items():
        print(key,":",value)

def factorial(n):
    """Recursive function to calculate factorial"""
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)



def filter_data():
    """Filters dataset using lambda function"""
    if not dataset:
        print("Dataset empty")
        return

    threshold = int(input("Enter threshold value: "))

    if isinstance(dataset[0], list):