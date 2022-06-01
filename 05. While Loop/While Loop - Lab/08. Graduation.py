name = input()
year = 1
grades_sum = 0
fails = 0

while year <= 12:
    grade = float(input())
    if grade < 4:
        fails += 1
    else:
        grades_sum += grade
        year += 1
        average_grade = grades_sum / 12
    if fails == 2:
        print(f"{name} has been excluded at {year} grade")
        break
else:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
