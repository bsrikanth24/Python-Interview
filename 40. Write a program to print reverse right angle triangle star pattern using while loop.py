"""
Description:
Same like program#39
"""

i = 1
while i <= 5:
    j = 5
    while j >= i:
        print('*', end=" ")
        j -= 1
    print()
    i += 1