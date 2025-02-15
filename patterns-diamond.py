
def printDiamondWithStars_v1(rows):
    #Upper diamond
    for i in range(1, rows + 1):
        str = " "*(rows - i) + "* "*i
        print("-"*(rows - i) + "*-"*i)
    
    #lower diamond
    for i in range (rows - 1, 0, -1):
        print("-"*(rows - i) + "*-"*i)


def printDiamondWithStars_v2(rows):
    """Prints a diamond shape with '*' characters of height n."""
    if rows % 2 == 0:
        rows += 1  # Make sure n is odd

    for i in range(rows):
        spaces = abs((rows // 2) - i)
        stars = rows - 2 * spaces
        print(" " * spaces + "*" * stars)



def printDiamondWithStars_v3(rows):
    for row in range(rows):
        str = ' ' * (rows - row - 1) + '*' * (2 * row + 1)
        print(str)
    for row in range(rows - 2, -1, -1):
        print(' ' * (rows - row - 1) + '*' * (2 * row + 1))


#printDiamondWithStars_v1(6)
#printDiamondWithStars_v2(8)
printDiamondWithStars_v3(5)