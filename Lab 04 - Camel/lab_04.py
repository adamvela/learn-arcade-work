import random


# Opening message of game
def main():
    print("Welcome to camel!")
    print("You have stolen a camel and need to escape.")
    print("The natives want their camel back, you need to survive")
    print("the trek and out run the natives.")

    # Starting variables
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    native_distance = -20
    drinks = 3

# Options for game
    done = False
    while not done:
        print("\nA.Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        choice = input("What is your choice? ")

        # Quitting the game
        if choice.lower() == "q":
            done = True
            print("You quit the game, have a good day.\n")

        # Status check
        elif choice.lower() == "e":
            print("\nHere is your status: ")
            print("You've traveled:", miles_traveled, "miles")
            print("The natives are:", miles_traveled - native_distance, "miles behind you.")
            print("You have:", drinks, "drinks left in your canteen. \n")

        # Stopping for the night
        elif choice.lower() == "d":
            print("Your camel is happy and you slept good.")
            camel_tiredness = 0
            native_new = random.randrange(7, 14)
            native_distance += native_new

        # Going full speed
        elif choice.lower() == "c":
            miles = random.randrange(10, 21)
            miles_traveled += miles
            print("You traveled", miles, "miles.")
            thirst += 1
            camel_tiredness += random.randrange(1, 3)
            native_new = random.randrange(7, 14)
            native_distance += native_new
            if random.randrange(20) == 0:
                print("You found an oasis!")
                drinks = 3
                camel_tiredness = 0
                thirst = 0

        # Going moderate speed
        elif choice.lower() == "b":
            miles = random.randrange(5, 13)
            miles_traveled += miles
            print("You traveled", miles, "miles.")
            thirst += 1
            camel_tiredness += 1
            native_new = random.randrange(7, 14)
            native_distance += native_new
            if random.randrange(20) == 0:
                print("You found an oasis!")
                drinks = 3
                camel_tiredness = 0
                thirst = 0

        # Taking a drink
        elif choice.lower() == "a":
            if drinks >= 1:
                thirst = 0
                drinks -= 1
                print("You took a drink. ")
            else:
                print("You have no drinks left. ")

        # Won the game
        if miles_traveled >= 200:
            done = True
            print("You made it across the desert! You win the game.")

        # Dying of thirst
        if not done:
            if thirst == 6:
                done = True
                print("You died of thirst!")
            elif thirst >= 4:
                print("You are thirsty. ")

        # Camel dying
        if not done:
            if camel_tiredness > 8:
                print("Your camel is dead.")
                native_distance = miles_traveled
            elif camel_tiredness > 5:
                print("Your camel is getting tired.")

        # Natives catch up
        if not done:
            if native_distance >= miles_traveled:
                done = True
                print("The natives caught you.")
            elif (miles_traveled - native_distance) <= 15:
                print("The natives are getting close")


main()
