# Practice Chicken Monkey

for number in range(101):
    print(number)

for number in range(100):
  if number % 5 == 0:
      print("Chicken")
  else:
    print(number)

for number in range(100):
  if number % 7 == 0:
      print("Monkey")
  else:
    print(number)

for number in range(100):
  if(number%7==0 and number%5==0):
      print("ChickenMonkey")
  else:
    print(number)
