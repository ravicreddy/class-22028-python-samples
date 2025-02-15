
'''

def print_multiples(n):
    for i in range(1, 11):
        print(n * i, end=" ")
    print()

def print_multpication_table():
    for i in range(1, 11):
        print_multiples(i, high)


print_multpication_table()
'''





def print_multiples(n, high):
    for i in range(1, high+1):
        print(n * i, end=" ")
    print()

def print_multpication_table(high):
    for i in range(1, high+1):
        print_multiples(i, high)


print_multpication_table(10)