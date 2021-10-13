
# Creating my class called room
class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []

    # Room 0
    room = Room("You are in the dining hall, there is a west hall leading north,\n"
                "and a south hall leading east.",
                3, 1, None, None)
    room_list.append(room)

    # Room 1
    room = Room("You are in  a royal castle in the South hall, a pass way leads north.\n"
                "The queen's bedroom is east, and a front yard going south."
                "There is a dining hall west.", 4, 2, 8, 0)
    room_list.append(room)

    # Room 2
    room = Room("You are in the queens bedroom, the east hall leads north, and the south hall leads west.",
                5, None, None, 1)
    room_list.append(room)

    # Room 3
    room = Room("You are in the west hall, the magic kitchen is north, the north hall\n"
                "is east, and the dining hall is south.",
                6, 4, 0, None)
    room_list.append(room)

    # Room 4
    room = Room("You are in the north hall, the east hall is east, the south hall is south, and\n"
                "the west hall is west.",
                None, 5, 1, 3)
    room_list.append(room)

    # Room 5
    room = Room("You are in the east hall, the north hall is west, the king's room is north,\n"
                "and the queen's bedroom is south.",
                7, None, 2, 4)
    room_list.append(room)

    # Room 6
    room = Room("You are in the magic kitchen, the king's room is east, and the west hall leads\n"
                "south.",
                None, 7, 3, None)
    room_list.append(room)

    # Room 7
    room = Room("You are in the king's bedroom the east hall leads south and the magic kitchen is west.",
                None, None, 5, 6)
    room_list.append(room)

    # Room 8
    room = Room("You are in the yard, the south hall leads north.", 1, None, None, None)
    room_list.append(room)

    current_room = 1

    done = False
    while not done:
        print("\n")
        print(room_list[current_room].description)

        # Going north
        user_input = input("What do you want to do? ")
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Going east
        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Going south
        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Going west
        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        if user_input.lower() == "q" or user_input.lower() == "quit":
            print("You have quit the game, thank you for playing.")
            done = True


main()
