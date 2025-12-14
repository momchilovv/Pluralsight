look_up = input("Enter an acronym to look up: ")

found = False
with open("software_acronyms.txt") as file:
    for line in file:
        if look_up in line:
            found = True
            print(f"{line}")
            break

if not found:
    print(f"{look_up} acronym was not found")