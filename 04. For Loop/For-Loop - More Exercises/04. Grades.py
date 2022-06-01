students = int(input())

tops = 0
very_goods = 0
goods = 0
fails = 0
average_grade = 0

for student in range(students):
    grade = float(input())
    if grade < 3:
        fails += 1
    elif grade < 4:
        goods += 1
    elif grade < 5:
        very_goods += 1
    elif grade <= 6:
        tops += 1
    average_grade += grade / students

tops_p = tops / students * 100
very_goods_p = very_goods / students * 100
goods_p = goods / students * 100
fails_p = fails / students * 100

print(f"Top students: {tops_p:.2f}%")
print(f"Between 4.00 and 4.99: {very_goods_p:.2f}%")
print(f"Between 3.00 and 3.99: {goods_p:.2f}%")
print(f"Fail: {fails_p:.2f}%")
print(f"Average: {average_grade:.2f}")
