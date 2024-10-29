import random

def minGrade(grades):
   grades.pop(grades.index(min(grades)))

def randomRemoval(grades):
    grades.remove(random.choice(grades))
    

def sortingReversing(grades):
    grades.sort(reverse = True)
    

def getAverage(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

def getTotal(grades):
    total = sum(grades)
    return total

def main():
    grades = []
    grade = ""
    while grade != -1:
        grade = int(input("Enter a grade or -1 to stop: "))
        if grade == -1:
            break
        else :
            grades.append(grade)
    print(grades)
    print("Removing lowest grade")
    minGrade( grades)
    print(grades)
    print("Removing a random grade")
    randomRemoval(grades)
    print(grades)
    print("Edit a grade")
    for num, item in enumerate(grades, start=1):
        print(f"{num}. {item}")
    edit = int(input("which grade do you want to edit: "))

    while edit < 0 or edit > num:
        edit = int(input("which grade do you wan to edit (Enter a number from the choices): "))

    grades[edit-1] = int (input("enter new grade: "))
    print(grades)
    print("Sorting and reversing list")
    sortingReversing(grades)
    print(grades)
    print("Getting grade total and average")
    print(f"Total: {getTotal(grades)}")
    print(f"Average: {getAverage(grades)}\n")

    print("\n" + "-"*15)
    print("Coded by samuel Simmons")

if __name__ == "__main__":
    main()

