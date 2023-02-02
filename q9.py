class sol:
   def parenthesis(self, str1):
        stack, char = [], {"(": ")", "{": "}", "[": "]"}
        for parenthesis1 in str1:
            if parenthesis1 in char:
                stack.append(parenthesis1)
            elif len(stack) == 0 or char[stack.pop()] != parenthesis1:
                return False
        return len(stack) == 0

a = input("Enter parenthesis :-  ")
print(sol().parenthesis(a))
