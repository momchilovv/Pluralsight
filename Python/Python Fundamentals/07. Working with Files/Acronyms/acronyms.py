file_path = "software_acronyms.txt"

def find_acronym(acronym):
    found = False
    with open(file_path) as file:
        for line in file:
            if acronym in line.split('-')[0]:
                found = True
                return line

    if not found:
        print(f"{acronym} acronym was not found")

def add_acronym(acronym, definition):
    with open(file_path, "a") as file:
        file.write(f"{acronym} - {definition}\n")

def remove_acronym(acronym):
    found = False

    with open(file_path) as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if line.split('-')[0].strip() != acronym:
                file.write(line)
            else:
                found = True
    if found:
        print(f"{acronym} was successfully removed from the list.")  
    else:
        print(f"{acronym} was not found.")          

def print_acronym(acronym):
    try:
        print(f"{acronym.split('-')[0]} - {acronym.split('-')[1]}")
    except:
        exit(0)

def main():
    while True:
        key = input("Enter A to Add, R to Remove, F to Find an acronym, or Q to Quit the program: ").lower()
        
        if key == 'a':
            acronym = input("Enter the acronym you want to add: ")
            definition = input("Enter the definition of that acronym: ")
            add_acronym(acronym, definition)

        elif key == 'r':
            acronym = input("Enter the acronym you want to remove: ")
            remove_acronym(acronym)

        elif key == 'f':
            acronym = input("Enter the acronym you want to find: ")
            print(find_acronym(acronym))

        elif key == 'q':
            print(f"Exiting program.")
            exit(0)

        else:
            print(f"'{key}' is not a valid keyboard shortcut.")

main()