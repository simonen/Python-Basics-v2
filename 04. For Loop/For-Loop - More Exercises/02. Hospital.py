days = int(input())
treated = 0
untreated = 0
doctors = 7

for day in range(1, days + 1):
    if day % 3 == 0:
        if treated < untreated:
            doctors += 1
    patients = int(input())
    if patients > doctors:
        untreated += patients - doctors
        treated += doctors
    else:
        treated += patients
        untreated += 0

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
