num = 0
tot = 0.0

while True:
      sval = input('Enter a number: ')
      if sval == 'done':
          break

      try:
          fval = float(sval)
      except :
          print('Invalid input')

      num = num + 1
      tot = tot + fval

print('All Done succssfully')

print('The number you wrote is: ', float(num))
print('The total of numbers: ', tot)
print('Average total is: ', num/tot)
