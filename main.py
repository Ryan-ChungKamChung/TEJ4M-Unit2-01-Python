#!/usr/bin/env python3

# Created by: Ryan C.
# Created on: February 2022
# Turing Machine that counts from 11-16

import time

# Replaces the current index with another number
def replace(number_list, index, insert_num):
    number_list[index] = insert_num


# Inserts a number into the list
def insert(number_list, index, insert_num):
    number_list.insert(index, insert_num)


# Removes a number from the list
def erase(number_list, index):
    number_list.pop(index)


# Moves index left
def move_left(index):
    index = index + 1
    return index


# Moves index right
def move_right(index):
    index = index - 1
    return index


# Pauses
def pause(seconds):
    time.sleep(seconds)


# Outputs list
def output(number_list, current_number):
    print(
        "\n"
        + str(current_number)
        + " == "
        + "".join([str(int) for int in number_list]),
        end="",
    )


# Counting logic
def main():
    number_list = [1, 0, 1, 1]
    index = len(number_list) - 1
    current_number = 12

    output(number_list, current_number - 1)

    while True:
        if index == -1:
            index = move_left(index)
            insert(number_list, index, "B")

        if number_list[index] == 0:
            replace(number_list, index, 1)
            output(number_list, current_number)
            current_number += 1

            while index < (len(number_list) - 1):
                index = move_left(index)
        elif number_list[index] == 1:
            replace(number_list, index, 0)
            index = move_right(index)
        else:
            replace(number_list, index, 1)
            output(number_list, current_number)
            break
        pause(1)

    print("\n\nDone.")


if __name__ == "__main__":
    main()
