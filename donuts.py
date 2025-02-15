def donuts(count):
  # +++your code here+++
  # LAB(begin solution)
  if count < 10:
    return 'Number of donuts: ' + str(count)
  else:
    return 'Number of donuts: many'
  # LAB(replace solution)
  # return
  # LAB(end solution)


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



test(donuts(4), 'Number of donuts: 4')
test(donuts(9), 'Number of donuts: 9')
test(donuts(10), 'Number of donuts: many')
test(donuts(99), 'Number of donuts: many')
test(donuts(-1), 'Number of donuts: many')
