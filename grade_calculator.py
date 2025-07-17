import random

def main():
    grades = []

    while True:
        entry = input("Enter a grade or -1 to stop: ")
        if entry == "-1":
            break
        grades.append(int(entry))

    print(grades)

    print("Removing the Lowest Grade")
    lowest = min(grades)
    index_of_lowest = grades.index(lowest)
    grades.pop(index_of_lowest)
    print(grades)

    print("Removing a Random Grade")
    random_grade = random.choice(grades)
    grades.remove(random_grade)
    print(grades)

    print("Edit a grade")
    while True:
        for i in range(len(grades)):
            print(f"{i+1}: {grades[i]}")
        choice = int(input("Enter the number of the corresponding grade to edit: "))
        if choice < 1 or choice > len(grades):
            print("Invalid choice. Try again.")
        else:
            new_grade = int(input("Enter the new grade: "))
            grades[choice - 1] = new_grade
            break
    print(grades)

    print("Sorting and Reversing the List")
    grades.sort()
    grades.reverse()
    print(grades)

    print("Generating Total and Average Grades")
    total = sum(grades)
    average = round(total / len(grades))
    print("Total of grades:", total)
    print("Average grade:", average)

    print("Completed by, Miguel Gomez")

if __name__ == "__main__":
    main()
