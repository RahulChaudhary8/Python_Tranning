# def process_string(input_string):
#     stack = Stack()
#     for char in input_string:
#         stack.push(char)
    
#     print("Stack after pushing characters:", stack)

#     while not stack.is_empty():
#         print("Popped:", stack.pop())

# # Example usage:
# input_string = "hello"
# process_string(input_string)

def isValid(s):
    st=[]
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='{' or s[i]=='[':
            st.append(s[i])
        elif s[i]==')' and st[-1]!='(': return False
        elif s[i]