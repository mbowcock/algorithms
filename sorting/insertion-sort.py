#!/usr/bin/python

def insertion_sort(unsorted_list):
    # sort unsorted_list in place using insertion sort and return sorted list
    input_length = len(unsorted_list)
    for i in range(1, input_length):
        key = unsorted_list[i]
        position = i
        while position > 0 and unsorted_list[position - 1] > key:
            unsorted_list[position] = unsorted_list[position -1]
            position = position - 1
        unsorted_list[position] = key
    return unsorted_list

if __name__ == "__main__":
    unsorted_list = [3,6,7,4,9,10,22,11,32,12]
    for e in insertion_sort(unsorted_list):
        print(e)

