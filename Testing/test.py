
# print(my_list)

# temp = my_list[2]
# my_list[2] = my_list[0]
# my_list[0] = temp

# my_list[0], my_list[2] = my_list[2], my_list[0]
# print(my_list)

# 15 57 14 33 72 79 26 56 42 40
# 14 57 15 33 72 79 26 56 42 40

def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


def insertion_sort(my_list):
    for key_pos in range(1, len(my_list)):
        key_val = my_list[key_pos]
        scan_position = key_pos - 1
        while(scan_position >= 0) and (my_list[scan_position] > key_val):  # worst: 50, avg 25
            my_list[scan_position + 1] = my_list[scan_position]
            scan_position -= 1

        my_list[scan_position + 1] = key_val


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
insertion_sort(my_list)
print(my_list)
