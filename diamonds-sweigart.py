
def main(writeToFile = False):
    print('Diamonds, by Al Sweigart al@inventwithpython.com')


    if writeToFile :
        fileHandle = open ("diamonds.txt", 'w')
    
    # Display diamonds of sizes 0 through 6:
    for diamondSize in range(0, 30):
        displayOutlineDiamond(diamondSize, fileHandle)
        write("\n") # Print a newline.
        displayFilledDiamond(diamondSize, fileHandle)
        write("\n") # Print a newline.

    if fileHandle :
        fileHandle.close()


def write(chars, fileHandle = None):
    if fileHandle != None:
        fileHandle.writeLines(chars)
    else :
        print(chars)


def displayOutlineDiamond(size):
# Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='') # Left side space.
        print('/', end='') # Left side of diamond.
        print(' ' * (i * 2), end='') # Interior of diamond.
        print('\\') # Right side of diamond.

    # Display the bottom half of the diamond:
    for i in range(size):
        print(' ' * i, end='') # Left side space.
        print('\\', end='') # Left side of diamond.
        print(' ' * ((size - i - 1) * 2), end='')
        print('/') # Right side of diamond.

def displayFilledDiamond(size):
    # Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='') # Left side space.
        print('/' * (i + 1), end='') # Left half of diamond.
        print('\\' * (i + 1)) # Right half of diamond.

    # Display the bottom half of the diamond:
    for i in range(size):
        print(' ' * i, end='') # Left side space.
        print('\\' * (size - i), end='') # Left side of diamond.
        print('/' * (size - i)) # Right side of diamond.


main()