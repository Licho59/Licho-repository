def toStr(n, base):
   '''Conversion of arbitrary 'n' integer number to the string in given 'base' of conversion - between binary and hexadecimal.'''  
   
   convertString = "0123456789ABCDEF"
   if n < base: # checking for the base case (first law of recursive algorithm - it needs the base case)
      return convertString[n]
   else:
      return toStr(n // base, base) + convertString[n % base] # the problem has been reduced to smaller one (second law) and recursive function has called itself (the third law)


print(toStr(1453, 16))
print(toStr(5555,9))
print(toStr(29408, 10))
