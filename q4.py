def pangram(s):
    if ('a'or'A')in s and('b'or'B')in s and('c'or'C')in s and('d'or'D')in s and('e'or'E')in s and('f'or'F')in s and('g'or'G')in s and('h'or'H')in s and('i'or'I')in s and('j'or'J')in s and('k'or"K")in s and('l'or'L')in s and('m'or'M')in s and('n'or'N')in s and('o'or'O')in s and('p'or'P')in s and('q'or'Q')in s and('r'or'R')in s and('s'or'S')in s and('t'or'T')in s and('u'or'U')in s and('v'or'V')in s and('w'or'W')in s and('x'or'X')in s and('y'or'Y')in s and('z'or'Z'):
        return True
    else:
        return False
#example
if pangram(input('enter a string to check whether a string is pangram:')):
    print('string is pangram')
else:
    print('string is not pangram')        
