import os
from datetime import datetime

class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # Add new journal entry
    def add_entry(self):
        entry = input("Enter your journal entry:\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(self.filename, "a") as file:
                file.write(f"\n[{timestamp}]\n{entry}\n")
            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied while writing the file.")

    # View all entries
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

                if data.strip() == "":
                    print("No journal entries found.")
                else:
                    print("\nYour Journal Entries:")
                    print("---------------------------------")
                    print(data)

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

    # Search entries
    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ")

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

                found = False
                print("\nMatching Entries:")
                print("---------------------------------")

                for line in lines:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True

                if not found:
                    print(f"No entries were found for the keyword: {keyword}")

        except FileNotFoundError:
            print("Error: The journal file does not exist.")

    # Delete all entries
    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")

        if confirm.lower() == "yes":
            try:
                os.remove(self.filename)
                print("All journal entries have been deleted.")

            except FileNotFoundError:
                print("No journal entries to delete.")

            except PermissionError:
                print("Error: Permission denied.")

        else:
            print("Deletion cancelled.")


# Main Menu
def main():

    journal = JournalManager()

    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("\nPlease select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            journal.add_entry()

        elif choice == "2":
            journal.view_entries()

        elif choice == "3":
            journal.search_entry()

        elif choice == "4":
            journal.delete_entries()

        elif choice == "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option from the menu.")


# Run program
if __name__ == "__main__":
    main()