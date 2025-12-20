students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    students.append({"name": name, "roll": roll})
    print("✅ Student added successfully")

def view_students():
    if not students:
        print("No students found")
    else:
        for s in students:
            print(f"Name: {s['name']}, Roll: {s['roll']}")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("✅ Student deleted")
            return
    print("❌ Student not found")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Bye 👋")
        break
    else:
        print("Invalid choice")
