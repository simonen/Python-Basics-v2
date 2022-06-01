judges = int(input())
presentation = input()
present_sum = 0
present_count = 0
while presentation != "Finish":
    grade_total = 0
    average = 0
    for j in range(1, judges + 1):
        grade = float(input())
        grade_total += grade
    present_average = grade_total / judges
    print(f"{presentation} - {present_average:.2f}.")
    present_sum += present_average
    presentation = input()
    present_count += 1
final_assess = present_sum / present_count
print(f"Student's final assessment is {final_assess:.2f}.")
