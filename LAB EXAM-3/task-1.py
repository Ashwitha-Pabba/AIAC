
def merge(left, right):
    merged = []
    i = j = 0
    # merge two sorted lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]  
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    data = [45, 12, 3, 67, 34, 21]
    print("Original:", data)
    sorted_data = merge_sort(data)
    print("Sorted:  ", sorted_data)
    assert sorted_data == sorted(data), "Merge sort result does not match Python's sorted()"