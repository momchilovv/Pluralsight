def find_acronym():
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

def add_acronym():
    acronym = input("Enter the acronym you want to add: ")
    defintion = input("Enter the definition of that acronym: ")

    with open("software_acronyms.txt", "a") as file:
        file.write(f"{acronym} - {defintion}\n")

def main():
    add_acronym()

main()