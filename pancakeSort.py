def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 0, -1):
        max_index = arr.index(max(arr[0:curr_size]))
        if max_index != curr_size - 1:
            arr = arr[:max_index+1][::-1] + arr[max_index+1:]
            arr = arr[:curr_size][::-1] + arr[curr_size:]
    return arr

arr = [23, 10, 5, 1, 18, 31, 16]
sorted_arr = pancake_sort(arr)
print("Pancake Sort:", sorted_arr)
