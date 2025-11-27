from typing import List, Dict, Optional

Student = Dict[str, List[int]]
students: List[Student] = []

def find_student(name: str) -> Optional[Student]:
    """Find a student by name (case-insensitive)."""
    return next((s for s in students if s['name'].lower() == name.lower()), None)

def add_student() -> None:
    """Add a new student to the list if not already present."""
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if find_student(name):
        print(f"Student '{name}' already exists.")
        return
    students.append({'name': name, 'grades': []})
    print(f"Student '{name}' added successfully.")

def add_grades() -> None:
    """Add grades to an existing student with validation."""
    name = input("Enter student name: ").strip()
    student = find_student(name)
    if not student:
        print(f"Student '{name}' not found.")
        return

    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()
        if grade_input.lower() == 'done':
            break
        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student['grades'].append(grade)
                avg = sum(student['grades']) / len(student['grades'])
                print(f"Grade added. Current average: {avg:.2f}")
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")

def calculate_average(grades: List[int]) -> Optional[float]:
    """Calculate average grade if grades are present."""
    return sum(grades) / len(grades) if grades else None

def generate_report() -> None:
    """Display a report of all students and overall statistics."""
    print("\n--- Student Report ---")
    averages = []

    for student in students:
        avg = calculate_average(student['grades'])
        if avg is not None:
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)
        else:
            print(f"{student['name']}'s average grade is N/A.")

    if averages:
        print(f"Max Average: {max(averages):.1f}")
        print(f"Min Average: {min(averages):.1f}")
        print(f"Overall Average: {sum(averages) / len(averages):.1f}")
    else:
        print("No valid grades available to calculate statistics.")

def find_top_student() -> None:
    """Identify and display the student with the highest average grade."""
    valid_students = [s for s in students if s['grades']]
    if not valid_students:
        print("No top student available. No grades entered.")
        return

    top = max(valid_students, key=lambda s: calculate_average(s['grades']) or 0)
    avg = calculate_average(top['grades'])
    print(f"The student with the highest average is {top['name']} with a grade of {avg:.1f}.")

def main() -> None:
    """Main loop to run the Student Grade Analyzer program."""
    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: ").strip())
            if choice == 1:
                add_student()
            elif choice == 2:
                add_grades()
            elif choice == 3:
                generate_report()
            elif choice == 4:
                find_top_student()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a numeric choice.")

if __name__ == "__main__":
    main()
