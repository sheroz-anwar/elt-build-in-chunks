# Student Records Management System

## Overview
A Python project that collects, validates, stores, and displays student records using a dictionary-based data structure.

## Features
- Validates student names, ages, classes, roll numbers, and marks.
- Prevents duplicate roll numbers.
- Handles invalid numeric input using reusable helper functions.
- Separates helper functions from the main program.

## Project Structure
- `students_records/main.py` — Runs the program.
- `students_records/helpers.py` — Contains input handling, validation, and student record functions.
- `.gitignore` — Excludes Python cache files from version control.

## Requirements
- Python 3.10 or newer.

## How to Run
Run the following command from the project root:

```bash
python students_records/main.py
```

## Concepts Practiced
- Functions and modular programming
- Dictionaries and sets
- Input validation and exception handling
- Code reuse and separation of responsibilities