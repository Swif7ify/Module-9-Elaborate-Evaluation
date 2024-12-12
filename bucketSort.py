def bucket_sort(arr):
    min_value = min(arr)
    max_value = max(arr)

    range_value = (max_value - min_value) / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        j = int((arr[i] - min_value) / range_value)
        if j == len(arr):
            j -= 1
        buckets[j].append(arr[i])

    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

    return arr

arr = [23, 10, 5, 1, 18, 31, 16]
sorted_arr = bucket_sort(arr)
print("Bucket Sort:", sorted_arr)