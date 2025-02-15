def print_binary_pattern(n):
    for i in range(n, 0, -2):
        print("1" * i)
        if i > 1:
            print("0" * (i - 1))

# Example usage
#print_binary_pattern(5) 




def print_binary_pattern3(n):
   for i in range(1, n + 1, 1):
       if(i%2 != 0):
           print("1"*(n-i+1))
       else :
           print("0"*(n-i+1))
   print()
#print_binary_pattern3(5)



count = 1
def doThis():
    global count
    count += 10

#doThis()
#print(count)



def my_str():
    message = "Python "
    new_message = message + " is " + message
    another_str = new_message.replace(message, "Great")
    return another_str

#print(my_str())







def my_list():
   lst1 = ["Python",  "is",  "great"]
   lst1.append("another")
   #lst2 = lst1
   #lst1[0] = "message"
   return lst1

print(my_list())







