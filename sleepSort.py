import time
import threading
def sleep_sort(arr):
    lock = threading.Lock()

    def sleep_and_print(value):
        time.sleep(value / 10)
        with lock:
            print(value)

    threads = []
    for value in arr:
        thread = threading.Thread(target=sleep_and_print, args=(value,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return arr

arr = [23, 10, 5, 1, 18, 31, 16]
sorted_arr = sleep_sort(arr)
print("Sleep Sort:", sorted_arr)
