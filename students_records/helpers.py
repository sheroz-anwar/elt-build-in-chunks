
import math


MIN_STUDENTS = 1
MAX_STUDENTS = 500

MIN_AGE = 18
MAX_AGE = 40

MIN_MARKS = 0.0
MAX_MARKS = 100.0


StudentRecord = dict[str, str | int | float]


def read_value(prompt: str, converter: type) -> int | float:
    """Read input and convert it to the requested numeric type."""

    while True:
        try:
            return converter(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_int(
    prompt: str,
    min_value: int,
    max_value: int | None = None,
) -> int:
    """Read an integer within the allowed range."""

    while True:
        value = read_value(prompt, int)

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
        value = read_value(prompt, float)

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
            print("Input cannot be empty. Please enter a value.")
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
            "hyphens, or apostrophes only."
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
            "Invalid class. Use letters or alphanumeric text; "
            "numbers alone are not allowed."
        )


def read_roll_number(existing_roll_numbers: set[str]) -> str:
    """Read a valid, unique roll number."""

    while True:
        roll_number = read_non_empty_text(
            "Enter roll number (e.g. 32-24): "
        )

        parts = roll_number.split("-")

        if (
            len(parts) != 2
            or not all(part.isdigit() for part in parts)
            or not all(int(part) > 0 for part in parts)
        ):
            print(
                "Invalid roll number. Use the format 32-24 "
                "with positive numbers on both sides."
            )
            continue

        if roll_number in existing_roll_numbers:
            print(
                "This roll number already exists. "
                "Please enter a different roll number."
            )
            continue

        return roll_number


def get_student(
    existing_roll_numbers: set[str],
) -> tuple[str, StudentRecord]:
    """Collect and return one student's roll number and record."""

    name = read_name()
    age = read_int("Enter student age: ", MIN_AGE, MAX_AGE)
    student_class = read_class()
    roll_number = read_roll_number(existing_roll_numbers)
    marks = read_float("Enter marks: ", MIN_MARKS, MAX_MARKS)

    student: StudentRecord = {
        "name": name,
        "age": age,
        "class": student_class,
        "marks": marks,
    }

    return roll_number, student


def get_students(
    number_of_students: int,
) -> dict[str, StudentRecord]:
    """Collect records for the requested number of students."""

    students: dict[str, StudentRecord] = {}

    for student_number in range(1, number_of_students + 1):
        print(
            f"\n--- Student {student_number} "
            f"of {number_of_students} ---"
        )

        roll_number, student = get_student(set(students))
        students[roll_number] = student

    return students


def display_students(
    students: dict[str, StudentRecord],
) -> None:
    """Display student records in a readable format."""

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
