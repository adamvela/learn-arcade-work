
def main():
    name_list = []
    my_file = open("super_villains.txt")
    for line in my_file:
        line = line.strip()
        print(line)
        name_list.append(line)
    my_file.close()

    print(name_list)
    print("There were", len(name_list), "names in the file.")

    # Linear search
    key = "Octavia the Siren"

    current_line_position = 0
    while current_line_position < len(name_list) and name_list[current_line_position] != key:
        current_line_position += 1

    if current_line_position < len(name_list):
        print("Found at", current_line_position)
    else:
        print("Not found.")


main()
