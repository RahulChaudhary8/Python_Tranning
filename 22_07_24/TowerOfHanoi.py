# def tower_of_hanoi(n, source, destination, auxiliary):
#     if n ==1:
#         print(f"Move disk 1 from {source} to {destination}")
#         return
#     tower_of_hanoi(n - 1, source, auxiliary, destination)
#     print(f"Move disk {n} from {source} to {destination}")
#     tower_of_hanoi(n - 1, auxiliary, destination, source)

# # Example usage:
# n = 3  # Number of disks
# tower_of_hanoi(n, 'A', 'C', 'B')




def toh(n,src,des,aux):
    if n <= 0:
        return
    toh(n-1,src,aux,des)
    print("Move ",src," To ",des)
    toh(n-1,aux,des,src)

def main():
    n = 3
    src,des,aux = 'A','C','B'
    toh(n,src,des,aux)
main()