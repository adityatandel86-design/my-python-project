

students = []   



def add_student():
    try:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        student = {
            "roll": roll,
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        print("Student added successfully!")

    except ValueError:
        print("Invalid age! Please enter numeric value.")



def display_students():
    if not students:
        print("No student records found.")
        return

    print("\n---- Student Records ----")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")



def search_student():
    roll = input("Enter Roll Number to search: ")

    for s in students:
        if s['roll'] == roll:
            print("Student Found!")
            print(f"Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
            return

    print("Student not found.")



def update_student():
    roll = input("Enter Roll Number to update: ")

    for s in students:
        if s['roll'] == roll:
            s['name'] = input("Enter new Name: ")
            s['age'] = int(input("Enter new Age: "))
            s['course'] = input("Enter new Course: ")
            print("Student record updated successfully!")
            return

    print("Student not found.")



def delete_student