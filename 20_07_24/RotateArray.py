def rotate_array(arr, k):
    # Use a stack to reverse the array
    stack = []

    # Normalize k to ensure it falls within the array length
    n = len(arr)
    k = k % n
    
    # Push all elements to the stack
    for i in range(n):
        stack.append(arr[i])
    
    # Pop elements to form the rotated array
    rotated = []
    for i in range(n - k):
        rotated.append(stack.pop(0))
    
    for i in range(k):
        rotated.insert(0, stack.pop())
    
    return rotated

def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("Original array is= ",arr)
    k = 3
    result = rotate_array(arr, k)
    print("Rotated array:", result)

main()
