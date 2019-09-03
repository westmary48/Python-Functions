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


# Leahs way to do this

# def chicken_monkey_run():
#   range_to_100 = range(1, 100)
#   for num in range_to_100:
#     if num % 5 == 0 and num % 7 == 0:
#       print("ChickenMonkey")
#       elif num % 5 == 0
#       print("Chicken")
#       elif num % 7 == 0:
#       print("monkey")
#     else:
#       print(num)

# for i in range(1, 101):
#   output = ""
#   if(i % 5 == 0):
#     output = f'{output}Chicken'
#   if (i % 7 == 0):
#     output = f'{output}Monkey'

#     print(output if output != "" else i)


