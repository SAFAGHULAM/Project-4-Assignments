def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Checking middle index {mid} → {arr[mid]}")
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

nums = list(map(int, input("Enter sorted numbers (space-separated): ").split()))
x = int(input("Enter number to search: "))

index = binary_search(nums, x)
if index != -1:
    print(f"\n✅ Found {x} at index {index}")
else:
    print(f"\n❌ {x} not found in the list")
