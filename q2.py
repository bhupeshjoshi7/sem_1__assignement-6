def palindrome(s):
    for i in range(int(len(s)/2)):
        if s[i]!=s[-(i+1)]:
            return False
    else:
        return True
#examples
print(palindrome(input('enter string to check whether it is palindrome:')))
        
