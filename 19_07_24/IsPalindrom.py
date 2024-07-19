def IsPalindrom(str):
    if len(str)<=1:
        return True
    if str[0]!=str[-1]:
        return False
    return IsPalindrom(str[1:-1])

def main():
    str=input("Enter String: ")
    ans=IsPalindrom(str)
    print(ans)
main()




