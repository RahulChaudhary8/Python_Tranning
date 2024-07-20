def permute(arr):
    # Base case
    if len(arr) == 1:
        return [arr]
    
    # Recursive case
    permutations = []
    for i in range(len(arr)):
        # Extract the current element
        current = arr[i]
        # Remaining elements
        remaining = arr[:i] + arr[i+1:]
        # Generate all permutations for the remaining elements
        for p in permute(remaining):
            permutations.append([current] + p)
    
    return permutations

# Example usage:
def main():
    arr = [1, 2, 3]
    permutations=permute(arr)
    print(f"Permutations of {arr} is: {permutations}")
   
main()