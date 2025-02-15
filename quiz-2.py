def play():
    print("play")

#print(play())


def calculate_range():
    for x in range (22, 23, 24):
        print (x)

#calculate_range()


def solve (a, b):
    return b if a == 0 else solve(b%a, a)

#print(solve(20, 50))



def sum(n, i):
    i += 1
    print(f"Calling sum for the + {i} the time")
    if n == 0 :
        return 0
    else:
        return sum(n-1, i) + n

print(sum(100, 0))