def add(a, b):
    return a+b
result = add(2,2)*2
#print (result)


def listAppend():
    list_a = [1,2,3]
    list_b = [4,5,6]
    list_a.append(list_b)
    return list_a;
#print(len(listAppend()))




def iteration_test(elemenets):
    for x in elemenets:
        return x
        y = x + 2

#print(iteration_test([10, 20, 30]))



def listReference():
    a = "ravi"

    list = [[1,2]]*2
    list[1][0] = 3
    return list
#print(listReference())


def sliceAndJoin():
    s1 = "Python"
    s2 = s1[::-1]
    s3 = "".join(reversed(s1))
    return s2 == s3
#print(sliceAndJoin())



def compareFloats():
    a = 0.1
    b = 0.2
    return a+b == 0.3
#print(compareFloats())


def overridingValues(x, y = 2):
    x = x + y
    y += 1
    print(x, y)


overridingValues(4, 7)