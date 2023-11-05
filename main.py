'''
While Loop:
-----------

Syntax:

while condition:
    statements

    

For Loop:
=========

Syntax:

for variable_name in sequence:
    statements


Sequences --> range(), string, list, tuple,set and dict
'''

# Nested Loops

'''
Loop:
    loop:

'''

n = int(input())

for row in range(1, n+1):
    for col in range(1, row+1):
        print(col, end=" ")
    print()