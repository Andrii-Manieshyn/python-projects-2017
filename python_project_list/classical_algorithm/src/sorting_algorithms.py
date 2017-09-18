"""
Sorting

Implement two types of sorting algorithms: Merge sort and bubble sort.

"""
from classical_algorithm.src.time_counter import count_time

@count_time
def qsort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return qsort(less)+equal+qsort(greater)
    else:
        return array

@count_time
def merge_sort(array):
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k]=lefthalf[i]
                i=i+1
            else:
                array[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            array[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1
    return array


if __name__ == '__main__':
    qsort([10, 9, 5, 6, 7, 1, 2, 0])