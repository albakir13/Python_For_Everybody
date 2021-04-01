xinput = input("Enter a Number: ")
try:
    ival = int(xinput)
except:
    ival = -1

if ival > 0 :
    print('✓ Nice work ✓')
else:
    print('✖ Not a Number! ✖')
