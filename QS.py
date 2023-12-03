import numpy as np
import matplotlib.pyplot as plt

def update_plot(arr):
    plt.bar(range(len(arr)), arr, color='blue')
    plt.show()
    plt.pause(0.05)

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursive calls
    quicksort(left)
    quicksort(right)

    # Concatenate the sorted left, middle, and right parts
    arr[:] = left + middle + right
    update_plot(arr)

# Manually provide array elements
array_to_sort = [2, 3, 1]

# Set up the initial plot
plt.bar(range(len(array_to_sort)), array_to_sort, color='blue')
plt.show()

# Call the quicksort function for visualization
quicksort(array_to_sort)