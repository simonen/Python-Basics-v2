movie = input()
seats = int(input())

student_total = 0
standard_total = 0
kid_total = 0
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while movie != "Finish":
    per_movie_tickets = 0
    for seat in range(1, seats + 1):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
        per_movie_tickets += 1
    percent_full = per_movie_tickets / seats * 100
    total_tickets += per_movie_tickets
    print(f"{movie} - {percent_full:.2f}% full.")
    movie = input()
    if movie == "Finish":
        break
    seats = int(input())

standard_percent = standard_tickets / total_tickets * 100
student_percent = student_tickets / total_tickets * 100
kid_percent = kids_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
