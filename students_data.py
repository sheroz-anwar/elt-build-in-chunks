import math


MIN_STUDENTS = 1
MAX_STUDENTS = 500

MIN_AGE = 18
MAX_AGE = 40

MIN_ROLL_NUMBER = 1

MIN_MARKS = 0.0
MAX_MARKS = 100.0


StudentRecord = dict[str, str | int | float]


def read_int(
    prompt: str,
    min_value: int,
    max_value: int | None = None,
) -> int:
    """Read an integer within the allowed range."""

    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if value < min_value:
            print(f"Value must be at least {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Value must not exceed {max_value}.")
            continue

        return value


def read_float(
    prompt: str,
    min_value: float,
    max_value: float,
) -> float:
    """Read a finite decimal number within the allowed range."""

    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not math.isfinite(value):
            print("Invalid input. Please enter a finite number.")
            continue

        if not min_value <= value <= max_value:
            print(
                f"Value must be between {min_value:g} "
                f"and {max_value:g}."
            )
            continue

        return value


def read_non_empty_text(prompt: str) -> str:
    """Read non-empty text and normalize whitespace."""

    while True:
        value = input(prompt).strip()
        value = " ".join(value.split())

        if not value:
            print("Input cannot be empty.")
            continue

        return value


def read_name() -> str:
    """Read a name containing letters and permitted separators."""

    while True:
        name = read_non_empty_text("Enter student name: ")

        valid_characters = all(
            char.isalpha() or char in " -'"
            for char in name
        )
        contains_letter = any(char.isalpha() for char in name)

        if valid_characters and contains_letter:
            return name

        print(
            "Invalid name. Use letters, spaces, "
            "hyphens or apostrophes only."
        )


def read_class() -> str:
    """Read a class containing letters and optionally numbers."""

    while True:
        student_class = read_non_empty_text(
            "Enter student class: "
        )

        contains_letter = any(
            char.isalpha() for char in student_class
        )

        valid_characters = all(
            char.isalpha() or char.isdigit() or char in " -_"
            for char in student_class
        )

        if contains_letter and valid_characters:
            return student_class

        print(
            "Invalid class. Enter letters or alphanumeric text, "
            "not numbers alone."
        )


def read_roll_number(existing_roll_numbers: set[int]) -> int:
    """Read a positive roll number that is not already in use."""

    while True:
        roll_number = read_int(
            "Enter roll number: ",
            MIN_ROLL_NUMBER,
        )

        if roll_number in existing_roll_numbers:
            print("This roll number already exists. Try another.")
            continue

        return roll_number


def get_student(
    existing_roll_numbers: set[int],
) -> tuple[int, StudentRecord]:
    """Collect and return one student's roll number and record."""

    name = read_name()

    age = read_int(
        "Enter student age: ",
        MIN_AGE,
        MAX_AGE,
    )

    student_class = read_class()

    roll_number = read_roll_number(existing_roll_numbers)

    marks = read_float(
        "Enter marks: ",
        MIN_MARKS,
        MAX_MARKS,
    )

    student: StudentRecord = {
        "name": name,
        "age": age,
        "class": student_class,
        "marks": marks,
    }

    return roll_number, student


def get_students(
    number_of_students: int,
) -> dict[int, StudentRecord]:
    """Collect records for the requested number of students."""

    students: dict[int, StudentRecord] = {}

    for student_number in range(1, number_of_students + 1):
        print(
            f"\n--- Student {student_number} "
            f"of {number_of_students} ---"
        )

        roll_number, student = get_student(set(students))
        students[roll_number] = student

    return students


def display_students(
    students: dict[int, StudentRecord],
) -> None:
    """Display student records in a readable format and as a dictionary."""

    print("\n========== STUDENT RECORDS ==========")

    for roll_number, student in students.items():
        print(f"\nRoll Number: {roll_number}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Class: {student['class']}")
        print(f"Marks: {student['marks']:g}")

    print("\n=====================================")
    print(f"Total students: {len(students)}")

    print("\nStudent dictionary:")
    print(students)


def main() -> None:
    """Run the student-records program."""

    number_of_students = read_int(
        "Enter number of students: ",
        MIN_STUDENTS,
        MAX_STUDENTS,
    )

    students = get_students(number_of_students)
    display_students(students)


if __name__ == "__main__":
    main()
