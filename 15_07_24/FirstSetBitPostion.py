def getFirstSetBitPostion(n):
    ans=1
    while n%2 !=1:
        n=n>>1
        ans+=1
    return ans


def main():
    n=int(input())
    ans=getFirstSetBitPostion(n)
    print(ans)
main()