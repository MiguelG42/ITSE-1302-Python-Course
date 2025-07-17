def main():
    student_info = {}

    student_info["Moe"] = {
        "ID": "21001",
        "GPA": 3.4,
        "Credits Completed": 45,
        "Grades": [88, 76, 90]
    }
    student_info["Larry"] = {
        "ID": "21002",
        "GPA": 3.1,
        "Credits Completed": 38,
        "Grades": [82, 74, 85]
    }
    student_info["Curly"] = {
        "ID": "21003",
        "GPA": 3.7,
        "Credits Completed": 50,
        "Grades": [91, 89, 94]
    }

    print("Full Student Information")
    print(student_info)
    print()

    print("Student Names List")
    for name in student_info:
        print(name)
    print()

    print("Student Information List")
    print("Name\tID\tGPA\tCredits\tGrades")
    for name, info in student_info.items():
        print(f"{name}\t{info['ID']}\t{info['GPA']}\t{info['Credits Completed']}\t{info['Grades']}")
    print()

    print("Larry has transcended beyond. Removing student's info from records")
    larry_info = student_info.get("Larry")
    print(f"Larry: {larry_info}")
    student_info.pop("Larry")
    print()

    print("Updated Student Information:")
    print(student_info)
    print()

    print("Student GPA List")
    for name in student_info:
        gpa = student_info.get(name, {}).get("GPA")
        print(f"{name}\t{gpa}")
    print()

    print("Graduation has concluded. Clearing Student Information...")
    student_info.clear()
    print("All student records exterminated via Dalek:")
    print(student_info)
    print()

    print("Completed by, Miguel Gomez")

if __name__ == "__main__":
    main()
