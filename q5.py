def f(string):
    listin=string.split('-')
    listin.sort()
    strout=''
    for i in listin:
        strout+=i
        if i!=listin[-1]:
            strout+='-'
    return strout
#example
print(f(input('enter a string:')))
