def printSpiral(arr):
    if not arr:
        return
    
    n = len(arr)
    m = len(arr[0])
    
    top, bottom = 0, n - 1
    left, right = 0, m - 1
    
    while top <= bottom and left <= right:
        # Print top row
        for i in range(left, right + 1):
            print(arr[top][i], end=" ")
        top += 1
        
        # Print right column
        for i in range(top, bottom + 1):
            print(arr[i][right], end=" ")
        right -= 1
        
        if top <= bottom:
            # Print bottom row
            for i in range(right, left - 1, -1):
                print(arr[bottom][i], end=" ")
            bottom -= 1
        
        if left <= right:
            # Print left column
            for i in range(bottom, top - 1, -1):
                print(arr[i][left], end=" ")
            left += 1

def main():
    arr = [[8, -3, 9, 2], [9, 3, 2, 8], [1, 10, 11, 15], [8, 9, 15, 14]]
    printSpiral(arr)
main()
