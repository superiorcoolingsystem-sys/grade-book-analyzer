# Name: hitesh
# roll no: 2501060090
# Project: Gradebook Analyzer

print("Welcome to Gradebook Analyzer")
print("This program analyzes student marks.\n")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g. 10).")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number (e.g. 75 or 85.5).")

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    scores = sorted(marks.values())
    n = len(scores)
    if n % 2 == 1:
        return scores[n // 2]
    else:
        return (scores[n//2 - 1] + scores[n//2]) / 2

def find_max(marks):
    return max(marks.values())

def find_min(marks):
    return min(marks.values())


while True:
    marks = {}
    total = get_positive_int("How many students? ")

    for i in range(total):
        name = input(f"Enter student name ({i+1}/{total}): ").strip()
        # keep asking until user enters a valid numeric mark
        score = get_float(f"Enter marks for {name}: ")
        marks[name] = score

    avg = calculate_average(marks)
    median = calculate_median(marks)
    highest = find_max(marks)
    lowest = find_min(marks)

    print("\n--- Analysis Summary ---")
    print("Average:", round(avg, 2))
    print("Median :", median)
    print("Highest Score:", highest)
    print("Lowest Score :", lowest)

    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"

    print("\n--- Grade Distribution ---")
    print("A :", list(grades.values()).count("A"))
    print("B :", list(grades.values()).count("B"))
    print("C :", list(grades.values()).count("C"))
    print("D :", list(grades.values()).count("D"))
    print("F :", list(grades.values()).count("F"))

    passed = [n for n, s in marks.items() if s >= 40]
    failed = [n for n, s in marks.items() if s < 40]

    print("\nPassed Students:", passed)
    print("Failed Students:", failed)

    print("\nName\tMarks\tGrade")
    print("---------------------------")
    for name in marks:
        print(f"{name}\t{marks[name]}\t{grades[name]}")

    again = input("\nDo you want to run again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using Gradebook Analyzer!")
        break