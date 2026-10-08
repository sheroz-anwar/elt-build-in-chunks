def get_student() -> dict:
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student_class = input("Enter student class: ")
    roll_number = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "class": student_class,
        "roll_number": roll_number,
        "marks": marks
    }

    return student


def get_students(n: int) -> list[dict]:
    students = []

    for _ in range(n):
        student = get_student()
        students.append(student)

    return students


def main() -> None:
    n = int(input("Enter number of students: "))
    students = get_students(n)

    print("\nStudent Records:")
    print(students)


if __name__ == "__main__":
    main()