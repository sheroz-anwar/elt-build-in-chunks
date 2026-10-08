def get_student() -> tuple[int, dict]:
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student_class = input("Enter student class: ")
    roll_number = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "class": student_class,
        "marks": marks
    }

    return roll_number, student


def get_students(n: int) -> dict:
    students = {}

    for _ in range(n):
        roll_number, student = get_student()

        if roll_number in students:
            print("Roll number already exists. Please try again.")
            continue

        students[roll_number] = student

    return students


def main() -> None:
    n = int(input("Enter number of students: "))
    students = get_students(n)

    print("\nStudent Records:")
    print(students)


if __name__ == "__main__":
    main()