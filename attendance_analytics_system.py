def display_menu():
    print("\n==========================================")
    print("CLASSROOM ATTENDANCE ANALYTICS SYSTEM")
    print("==========================================")
    print("1. Record Attendance")
    print("2. View Attendance Summary")
    print("3. Exit")


def get_class_information():
    class_name = input("Enter Class Name      : ")
    subject_name = input("Enter Subject Name    : ")

    while True:
        try:
            total_students = int(input("Enter Total Students  : "))
            if total_students > 0:
                break
            else:
                print("Total students must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    return class_name, subject_name, total_students


def record_attendance(total_students):
    present = 0
    absent = 0

    for i in range(1, total_students + 1):

        while True:
            status = input(f"Student {i} : ").upper()

            if status == "P":
                present += 1
                break

            elif status == "A":
                absent += 1
                break

            else:
                print("Invalid Attendance Status.")
                print("Please Enter Again.")
                continue

    return present, absent


def calculate_attendance(present, absent, total_students):

    percentage = (present / total_students) * 100

    if percentage >= 90:
        status = "Excellent"
    elif percentage >= 75:
        status = "Good"
    else:
        status = "Poor"

    return percentage, status


def display_report(class_name, subject_name, total_students,
                   present, absent, percentage, status):

    print("\n==========================================")
    print("CLASS ATTENDANCE REPORT")
    print("==========================================")
    print(f"Class Name          : {class_name}")
    print(f"Subject             : {subject_name}")
    print(f"Total Students      : {total_students}")
    print(f"Present Students    : {present}")
    print(f"Absent Students     : {absent}")
    print(f"Attendance Rate     : {percentage:.2f}%")
    print(f"Attendance Status   : {status}")
    print("==========================================")

    # Bonus Challenge 1 (ASCII Attendance Chart)
    print("\nAttendance Chart")
    print(f"Present : {'*' * present}")
    print(f"Absent  : {'*' * absent}")


def main():

    classes_processed = 0
    attendance_history = []

    while True:

        display_menu()

        choice = input("Enter Choice : ")

        if choice == "1":

            class_name, subject_name, total_students = get_class_information()

            present, absent = record_attendance(total_students)

            percentage, status = calculate_attendance(
                present, absent, total_students)

            display_report(
                class_name,
                subject_name,
                total_students,
                present,
                absent,
                percentage,
                status
            )

            classes_processed += 1

            attendance_history.append({
                "class": class_name,
                "subject": subject_name,
                "percentage": percentage
            })

            again = input("\nWould you like to return to the main menu? (Y/N): ").upper()

            if again == "N":
                print("\nClasses Processed :", classes_processed)

                if attendance_history:
                    top_class = max(attendance_history,
                                    key=lambda x: x["percentage"])

                    print("\nTop Performing Class")
                    print("---------------------")
                    print(f"Class      : {top_class['class']}")
                    print(f"Subject    : {top_class['subject']}")
                    print(f"Attendance : {top_class['percentage']:.2f}%")

                print("\nThank You!")
                break

        elif choice == "2":

            if classes_processed == 0:
                print("\nNo attendance record available.")

            else:
                print("\n==========================================")
                print("ATTENDANCE SUMMARY")
                print("==========================================")
                print(f"Classes Processed : {classes_processed}")

                for record in attendance_history:
                    print(f"{record['class']} ({record['subject']}) - {record['percentage']:.2f}%")

        elif choice == "3":

            print("\nClasses Processed :", classes_processed)

            if attendance_history:
                top_class = max(attendance_history,
                                key=lambda x: x["percentage"])

                print("\nTop Performing Class")
                print("---------------------")
                print(f"Class      : {top_class['class']}")
                print(f"Subject    : {top_class['subject']}")
                print(f"Attendance : {top_class['percentage']:.2f}%")

            print("\nProgram Ended.")
            break

        else:
            print("Invalid Choice. Please try again.")
            continue


main()