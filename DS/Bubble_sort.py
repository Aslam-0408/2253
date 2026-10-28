def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
salaries = [50000, 30000, 45000, 25000, 60000]
bubble = salaries.copy()
selection = salaries.copy()
bubble_sort(bubble)
selection_sort(selection)
print("Original Salaries:", salaries)
print("Bubble Sort:", bubble)
print("Selection Sort:", selection)