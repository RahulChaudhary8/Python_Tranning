def sort_Arr_XOR(arr)

n=len(arr)
for i in range(1,n):
    for j in range(1,n-i-1):
        if arr[j]^arr[j+1]:
            arr[j], arr[j]=arr[j],arr[j+1]


arr=[2,3,9,2,9,7,4,5,4,5]
