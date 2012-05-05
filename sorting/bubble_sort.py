#!/usr/bin/python

def bubble_sort(unsorted_list):
    list_length = len(unsorted_list)
    for i in range(list_length - 1):
        for j in range(list_length - i- 1 ):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list

if __name__ == "__main__":
    unsorted_list = [22, 3, 6, 9, 2, 10, 4, 7, 5, 3]
    for e in bubble_sort(unsorted_list):
        print(e)
