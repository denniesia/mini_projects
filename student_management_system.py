# Dictionary to store student records
students = {}


def add_student(name, age, grade, subjects):
    """
    Add a new student record.
    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.
    """
    # Code to add a new student record
    if name in students:
        print(f"Student {name} already exists.")
    else:
        # Add the student record to the dictionary
        students[name] = {
            "age": age,
            "grade": grade,
            "subjects": subjects
        }
        print(f"Student {name} has been added.")


def update_student(name):
    """
    Update an existing student record.
    Args:
    - name (str): The name of the student whose record is to be updated.
    """
    # Check if the student exists
    # Prompt the user to update fields and keep current values if fields are empty
    # Code to update the student's record
    if name not in students:
        print(f'Student {name} does not exist in the database. Thus the data cannot be upgraded.')
    else:
        current_age = students[name]['age']
        current_grade = students[name]['grade']
        current_subjects = students[name]['subjects']

        print(f"\nUpdating record for {name}:")
        print(f"Current age: {current_age}")
        print(f"Current grade: {current_grade}")
        print(f"Current subjects: {', '.join(current_subjects)}")

        new_age = input(f"Enter new age (leave blank to keep {current_age}): ")
        new_grade = input(f"Enter new grade (leave blank to keep {current_age}): ")
        new_subjects = input(f"Enter new subjects (comma-separated, leave blank to keep current subjects): ")

        if new_age.split():
            students[name]['age'] = int(new_age)
        if new_grade.split():
            students[name]['grade'] = float(new_grade)
        if new_subjects.split():
            students[name]['subjects'] = [subject.strip() for subject in new_subjects.split(',')]

        print(f"Student {name}'s record has been updated.\n")

def delete_student(name):
    """
    Delete a student record based on the student's name.
    Args:
    - name (str): The name of the student to delete.
    """
    # Check if the student exists
    # Code to delete the student's record
    if name not in students:
        print(f"Student name {name} is not found.")
    else:
        del students[name]
        print(f"Student name {name} has been successfully deleted.")


def search_student(name):
    """
    Search for a student by name and return their record.
    Args:
    - name (str): The name of the student to search for.
    """
    # Check if the student exists
    # Code to return the student's record
    if name not in students:
        print(f'Student name {name} does not exist.')
    else:
        print(f'{name} found!')
        print(f"Student age: {students[name]['age']}")
        print(f"Student grade: {students[name]['grade']}")
        print(f"Student subjects: {', '.join(students[name]['subjects'])}")


def list_all_students():
    """
    List all student records.
    """
    # Check if there are any student records
    # Code to list all students
    if students:
        for student, student_info in students.items():
            age = student_info['age']
            grade = student_info['grade']
            subjects = student_info['subjects']
            print(f"Student name: {student}")
            print(f"Student age: {age}")
            print(f"Student grade: {grade}")
            print(f"Student subjects: {', '.join(subjects)}")

    else:
        print("No student's records!")


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif choice == '2':
            # Prompt for student name to update
            name = input("Enter student's name to update: ")
            # Call the update_student function
            update_student(name)
        elif choice == '3':
            # Prompt for student name to delete
            name = input("Enter student's name to delete: ")
            # Call the delete_student function
            delete_student(name)
        elif choice == '4':
            # Prompt for student name to search
            name = input("Enter student's name to search: ")
            # Call the search_student function
            search_student(name)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()