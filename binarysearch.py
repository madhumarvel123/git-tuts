def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # target found at index mid
        elif arr[mid] < target:
            low = mid + 1  # search in right half
        else:
            high = mid - 1  # search in left half

    return -1  # target not found

# Example usage
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 9

result = binary_search(numbers, target)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")
