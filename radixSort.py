def radix_sort(arr):
    max_num = max(arr)
    digits = len(str(abs(max_num)))

    place = 1

    for _ in range(digits):
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = (num // place) % 10
            buckets[digit].append(num)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        place *= 10

    return arr

arr = [23, 10, 5, 1, 18, 31, 16]
sorted_arr = radix_sort(arr)
print("Radix Sort:", sorted_arr)