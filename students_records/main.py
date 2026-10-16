
from helpers import (
    MAX_STUDENTS,
    MIN_STUDENTS,
    StudentRecord,
    display_students,
    get_students,
    read_int,
)


def main() -> None:
    """Run the student-records program."""

    number_of_students = read_int(
        "Enter number of students: ",
        MIN_STUDENTS,
        MAX_STUDENTS,
    )

    students: dict[str, StudentRecord] = get_students(
        number_of_students
    )

    display_students(students)


if __name__ == "__main__":
    main()
