
import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    dictionary = open("dictionary.txt")
    dictionary_list = []
    for line in dictionary:
        line = line.strip()
        dictionary_list.append(line)
    dictionary.close()
    print("---Linear Search---")

    my_file = open("AliceInWonderLand200.txt")
    line_number = 0

    for line in my_file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            current_position = 0
            while current_position < len(dictionary_list) and dictionary_list[current_position] != word.upper():
                current_position += 1
            if current_position == len(dictionary_list):
                print("Line", line_number, "possible misspelled word:", word)

    my_file.close()
    print("\n---Binary Search---")

    my_file = open("AliceInWonderLand200.txt")
    line_number = 0
    for line in my_file:
        line_number += 1
        word_list = split_line(line)

        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("Line", line_number, "possible misspelled word:", word)


main()
