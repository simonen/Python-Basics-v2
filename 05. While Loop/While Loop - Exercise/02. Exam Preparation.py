fails_limit = int(input())
problem = input()
problem_count = 0
last_problem = ''
fails = 0
grade_sum = 0
average_score = 0

while problem != "Enough":
    grade = float(input())
    if grade <= 4:
        fails += 1
    if fails == fails_limit:
        print(f"You need a break, {fails} poor grades.")
        break
    problem_count += 1
    grade_sum += grade
    average_score = grade_sum / problem_count
    last_problem = problem
    problem = input()
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem}")
