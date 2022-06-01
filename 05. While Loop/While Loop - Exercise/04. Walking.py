total_steps = 0
is_home = False

while total_steps < 10000:
    steps_out = input()
    if steps_out == "Going home":
        steps_out = int(input())
        is_home = True
    total_steps += int(steps_out)
    if is_home:
        break
difference = abs(10000 - total_steps)

if total_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")