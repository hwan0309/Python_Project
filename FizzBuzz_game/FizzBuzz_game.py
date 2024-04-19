target = 100
for number in range(1,target + 1):
    #3 or 5 = FizzBuzz
  if number % 3 ==0 and number % 5 == 0:
    print("FizzBuzz")
    #3 = Fizz
  elif number % 3 == 0:
    print("Fizz")
    #5 = Buzz
  elif number % 5 == 0:
    print("Buzz")
  else:
    print (number)