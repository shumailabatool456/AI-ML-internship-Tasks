# ============================================
# UNIVERSITY STUDENT MANAGEMENT SYSTEM
# ============================================

students = {}
student_counter = 1

# Generate Student ID

def generate_student_id():
    global student_counter
    student_id = f"STD{student_counter:03d}"
    student_counter += 1
    return student_id

# Calculate Percentages

def calculate_percentage(matric, fsc):
    matric_percentage = (matric / 1100) * 100
    fsc_percentage = (fsc / 1100) * 100
    overall_percentage = (matric_percentage + fsc_percentage) / 2

    scholarship = "Eligible" if overall_percentage >= 70 else "Not Eligible"

    return (
        round(matric_percentage, 2),
        round(fsc_percentage, 2),
        round(overall_percentage, 2),
        scholarship,
    )



# Add Student

def add_student():
    student_id = generate_student_id()

    print("\n========== ADD STUDENT ==========\n")

    name = input("Enter Student Name : ")
    age = int(input("Enter Age          : "))
    gender = input("Enter Gender       : ")
    city = input("Enter City         : ")

    matric = float(input("Enter Matric Marks : "))
    fsc = float(input("Enter FSc Marks    : "))

    matric_per, fsc_per, overall_per, scholarship = calculate_percentage(
        matric, fsc
    )

    students[student_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "city": city,
        "matric": matric,
        "fsc": fsc,
        "matric_per": matric_per,
        "fsc_per": fsc_per,
        "overall_per": overall_per,
        "scholarship": scholarship,
    }

    print("\nStudent Added Successfully.")
    print("Generated Student ID :", student_id)



# Search Student

def search_student():
    print("\nSearch By")
    print("1. Student ID")
    print("2. Student Name")

    choice = input("Enter Choice : ")

    found = False

    if choice == "1":
        sid = input("Enter Student ID : ").upper()

        if sid in students:
            display_profile(sid)
        else:
            print("\nStudent Record Not Found.")

    elif choice == "2":
        name = input("Enter Student Name : ").lower()

        for sid, student in students.items():
            if student["name"].lower() == name:
                display_profile(sid)
                found = True
                break

        if not found:
            print("\nStudent Record Not Found.")

    else:
        print("Invalid Choice")



# Display Student Profile

def display_profile(student_id):
    student = students[student_id]

    print("\n===================================")
    print("Student Found")
    print("===================================")

    print(f"Student ID         : {student_id}")
    print(f"Student Name       : {student['name']}")
    print(f"Age                : {student['age']}")
    print(f"Gender             : {student['gender']}")
    print(f"City               : {student['city']}")

    print()

    print(f"Matric Marks       : {student['matric']}")
    print(f"FSc Marks          : {student['fsc']}")

    print()

    print(f"Matric Percentage  : {student['matric_per']}%")
    print(f"FSc Percentage     : {student['fsc_per']}%")
    print(f"Average Percentage : {student['overall_per']}%")

    print()

    print(f"Scholarship Status : {student['scholarship']}")



# Update Student

def update_student():
    sid = input("\nEnter Student ID : ").upper()

    if sid not in students:
        print("\nStudent Record Not Found.")
        return

    matric = float(input("Enter New Matric Marks : "))
    fsc = float(input("Enter New FSc Marks    : "))

    matric_per, fsc_per, overall_per, scholarship = calculate_percentage(
        matric, fsc
    )

    students[sid]["matric"] = matric
    students[sid]["fsc"] = fsc
    students[sid]["matric_per"] = matric_per
    students[sid]["fsc_per"] = fsc_per
    students[sid]["overall_per"] = overall_per
    students[sid]["scholarship"] = scholarship

    print("\nStudent Record Updated Successfully.")


# Delete Student

def delete_student():
    sid = input("\nEnter Student ID : ").upper()

    if sid not in students:
        print("\nStudent Record Not Found.")
        return

    confirm = input("Are you sure? (Y/N): ").upper()

    if confirm == "Y":
        del students[sid]
        print("\nStudent Record Deleted Successfully.")
    else:
        print("\nDeletion Cancelled.")



# Show All Students

def show_all_students():

    if len(students) == 0:
        print("\nNo Student Records Available.")
        return

    print("\n===================================")
    print("STUDENT LIST")
    print("===================================")

    for sid, student in students.items():

        print(f"ID                 : {sid}")
        print(f"Name               : {student['name']}")
        print(f"Average Percentage : {student['overall_per']}%")
        print(f"Scholarship        : {student['scholarship']}")

        print("-----------------------------------")



# Class Statistics

def class_statistics():

    if len(students) == 0:
        print("\nNo Student Records Available.")
        return

    percentages = []

    scholarship_count = 0

    for student in students.values():
        percentages.append(student["overall_per"])

        if student["scholarship"] == "Eligible":
            scholarship_count += 1

    print("\n========== CLASS STATISTICS ==========\n")

    print("Total Students       :", len(students))
    print("Average Percentage   :", round(sum(percentages) / len(percentages), 2))
    print("Highest Percentage   :", max(percentages))
    print("Lowest Percentage    :", min(percentages))
    print("Scholarship Students :", scholarship_count)

# Main Menu

def menu():

    while True:

        print("\n===========================================")
        print("UNIVERSITY STUDENT MANAGEMENT SYSTEM")
        print("===========================================")

        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Show All Students")
        print("6. Class Statistics")
        print("7. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_student()

        elif choice == "2":
            search_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            show_all_students()

        elif choice == "6":
            class_statistics()

        elif choice == "7":

            print("\n===========================================")
            print("Thank You for Using")
            print("University Student Management System")
            print("===========================================")

            break

        else:
            print("\nInvalid Choice. Try Again.")
1

menu()