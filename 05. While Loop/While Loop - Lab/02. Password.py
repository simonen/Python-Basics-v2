username = input()
password = input()
entered_password = input()

while password != entered_password:
    entered_password = input()
print(f"Welcome {username}!")