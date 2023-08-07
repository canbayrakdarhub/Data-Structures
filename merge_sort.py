
def merge_sort(list):
    #Sort a list in an ascending order.
    #Returns a new sorted list.
    #Divide : Find the midpoint of the list and divide into sub-lists.
    #Conquer : Recursively sort the sublists created.
    #Combine : Merge the sorted sublists.

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):
    #Divide the unsorted list at midpoint into sublists, returns two sublists, left and right

    mid = len(list)//2
    left = list[0:mid]
    right = list[mid:]

    return left, right


def merge(left,right):
    #Merges two lists, sorting them in the process and returns a new merged list

    list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list.append(left[i])
            i = i+1
        else:
            list.append(right[j])
            j = j+1

    while i<len(left):
        list.append(left[i])
        i = i+1

    while j<len(right):
        list.append(right[j])
        j = j+1

    return list

alist = [54,62,93,17,77,31,44,55,20]
l = merge_sort(alist)
print(l)


def verify_sorted(list):
    n = len(list)
    if n== 0 or n==1:
        return True

    return list[0] < list [1] and verify_sorted(list[1:])

print(verify_sorted(l))
