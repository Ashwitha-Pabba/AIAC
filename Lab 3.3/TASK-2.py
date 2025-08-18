def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    Time Complexity: O(n²)
    """
    n = len(arr)
    arr_copy = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    
    return arr_copy

def selection_sort(arr):
    """
    Selection Sort Algorithm
    Time Complexity: O(n²)
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    
    return arr_copy

def insertion_sort(arr):
    """
    Insertion Sort Algorithm
    Time Complexity: O(n²)
    """
    arr_copy = arr.copy()
    
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    
    return arr_copy

def quick_sort(arr):
    """
    Quick Sort Algorithm
    Time Complexity: O(n log n) average, O(n²) worst case
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """
    Merge Sort Algorithm
    Time Complexity: O(n log n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    print("=== SORTING ALGORITHMS DEMONSTRATION ===\n")
    
    # Example 1: Simple integer array
    print("Example 1: Integer Array")
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Input:  {numbers}")
    
    print(f"Bubble Sort:    {bubble_sort(numbers)}")
    print(f"Selection Sort: {selection_sort(numbers)}")
    print(f"Insertion Sort: {insertion_sort(numbers)}")
    print(f"Quick Sort:     {quick_sort(numbers)}")
    print(f"Merge Sort:     {merge_sort(numbers)}")
    print(f"Python Built-in: {sorted(numbers)}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Array with duplicates
    print("Example 2: Array with Duplicates")
    duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Input:  {duplicates}")
    
    print(f"Bubble Sort:    {bubble_sort(duplicates)}")
    print(f"Selection Sort: {selection_sort(duplicates)}")
    print(f"Insertion Sort: {insertion_sort(duplicates)}")
    print(f"Quick Sort:     {quick_sort(duplicates)}")
    print(f"Merge Sort:     {merge_sort(duplicates)}")
    print(f"Python Built-in: {sorted(duplicates)}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: Already sorted array
    print("Example 3: Already Sorted Array")
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Input:  {sorted_arr}")
    
    print(f"Bubble Sort:    {bubble_sort(sorted_arr)}")
    print(f"Selection Sort: {selection_sort(sorted_arr)}")
    print(f"Insertion Sort: {insertion_sort(sorted_arr)}")
    print(f"Quick Sort:     {quick_sort(sorted_arr)}")
    print(f"Merge Sort:     {merge_sort(sorted_arr)}")
    print(f"Python Built-in: {sorted(sorted_arr)}")
    
    print("\n" + "="*50 + "\n")
    
    # Example 4: Reverse sorted array
    print("Example 4: Reverse Sorted Array")
    reverse_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Input:  {reverse_arr}")
    
    print(f"Bubble Sort:    {bubble_sort(reverse_arr)}")
    print(f"Selection Sort: {selection_sort(reverse_arr)}")
    print(f"Insertion Sort: {insertion_sort(reverse_arr)}")
    print(f"Quick Sort:     {quick_sort(reverse_arr)}")
    print(f"Merge Sort:     {merge_sort(reverse_arr)}")
    print(f"Python Built-in: {sorted(reverse_arr)}")
    
    print("\n" + "="*50 + "\n")
    
    # Interactive sorting
    print("Interactive Sorting Demo")
    try:
        user_input = input("Enter numbers separated by spaces (e.g., 5 2 8 1): ")
        user_numbers = [int(x) for x in user_input.split()]
        
        print(f"\nYour input: {user_numbers}")
        print(f"Sorted (Quick Sort): {quick_sort(user_numbers)}")
        print(f"Sorted (Python Built-in): {sorted(user_numbers)}")
        
    except ValueError:
        print("Invalid input! Please enter numbers separated by spaces.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")

if __name__ == "__main__":
    main()
