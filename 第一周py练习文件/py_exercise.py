numbers = [12,37,56,3,8,42]
even = []
odd = []
while len(numbers) > 0:
      number = numbers.pop()
      if (number % 2 == 0 ):
         even.append (number)
      else:
         odd.append (number)
