import time
# Problem 1 - Value Swap (2pts)
# Swap the values 18 and 38 in the list below.  Print the new list.
my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]


def eighteen_thirty_eight_switch(list_to_be_switched=[18, 38]):
    for i in range(len(list_to_be_switched)):
        if list_to_be_switched[i] == 18:
            list_to_be_switched[i] = 38
        elif list_to_be_switched[i] == 38:
            list_to_be_switched[i] = 18


print(my_list)
eighteen_thirty_eight_switch(list_to_be_switched=my_list)
print(my_list)

# Problem 2 - Selection Sort (8 pts)
# Make a selection sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me = [655, 722, 736, 314, 59, 778, 632, 477, 230, 556, 353, 769, 622, 731, 683, 233, 524, 186, 694, 507, 443, 833, 270, 373, 567, 775, 34]


def selection_sort(leest):
    for current_position in range(len(leest)):
        smallest_position = current_position
        for scan_position in range(current_position + 1, len(leest)):
            if leest[scan_position] < leest[smallest_position]:
                smallest_position = scan_position
        leest[current_position], leest[smallest_position] = leest[smallest_position], leest[current_position]


selection_sort(sort_me)
print(sort_me)

# Problem 3 - Insertion Sort (8 pts)
# Make an insertion sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me2 = [551, 138, 802, 954, 569, 372, 454, 366, 936, 959, 958, 202, 474, 658, 108, 424, 523, 611, 557, 0, 733, 903, 788, 850, 11, 12, 975]


def insertion_sort(leest):
    for key_position in range(1, len(leest)):
        key_value = leest[key_position]
        scan_position = key_position - 1
        while (scan_position >= 0) and (leest[scan_position] > key_value):
            leest[scan_position + 1] = leest[scan_position]
            scan_position -= 1
        # Make the swap.
        leest[scan_position + 1] = key_value


insertion_sort(sort_me2)
print(sort_me2)

# Problem 4 - Efficiency? (10 pts)
# Modify your two functions so that they track the number of times
# you iterate through the big loop, and the inner loop of the sort.  Ask if you have questions.
# Make the functions print each value (times through big loop and inner loop).  
# Run each sort on the list below with the results of the efficiency (loop counts) printed.

sort_me3 = [77, 29, 59, 69, 86, 40, 47, 40, 74, 44, 58, 78, 9, 8, 13, 99, 3, 57, 19, 48, 55, 50, 94, 69, 98, 30, 37, 29, 40, 29, 36, 32, 26, 85, 61, 51, 70, 96, 90, 89, 91, 88, 68, 4, 4, 74, 15, 72, 5, 91, 76, 6, 56, 80, 72, 87, 63, 86, 48, 24, 17, 23, 30, 41, 7, 64, 16, 19, 40, 63, 14, 95, 44, 58, 1, 6, 45, 55, 52, 54, 44, 36, 50, 6, 96, 66, 8, 46, 48, 48, 75, 25, 39, 30, 70, 44, 38, 90, 49, 70]
_sort_me3 = sort_me3[:]

# time.perf_counter() # grabs current time of the program


def selection_sort(leest):
    times_gone_through_big_loop = 0
    times_gone_through_small_loop = 0
    for current_position in range(len(leest)):
        smallest_position = current_position
        for scan_position in range(current_position + 1, len(leest)):
            if leest[scan_position] < leest[smallest_position]:
                smallest_position = scan_position
            times_gone_through_small_loop += 1
        times_gone_through_big_loop += 1
        leest[current_position], leest[smallest_position] = leest[smallest_position], leest[current_position]
    print("Selection sort went through the big loop", times_gone_through_big_loop, "times.")
    print("Selection sort went through the small loop", times_gone_through_small_loop, "times.")


def insertion_sort(leest):
    times_gone_through_big_loop = 0
    times_gone_through_small_loop = 0
    for key_position in range(1, len(leest)):
        key_value = leest[key_position]
        scan_position = key_position - 1
        while (scan_position >= 0) and (leest[scan_position] > key_value):
            leest[scan_position + 1] = leest[scan_position]
            scan_position -= 1
            times_gone_through_small_loop += 1
        # Make the swap.
        leest[scan_position + 1] = key_value
        times_gone_through_big_loop += 1
    print("Insertion sort went through the big loop", times_gone_through_big_loop, "times.")
    print("Insertion sort went through the small loop", times_gone_through_small_loop, "times.")


selection_sort(sort_me3)
print(sort_me3)
insertion_sort(_sort_me3)
print(_sort_me3)
