# Activities for kids

running_kids = ["Pam", "Sam", "Andrea", "Will"]
for run in running_kids:
  print(f"{run} ran like a fool")

swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
for swing in swinging_kids:
  print(f"{swing} loves to swing really high!")


sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
for slid in sliding_kids:
  print(f"{slid} slid down the slide!")

hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]
for hid in hiding_kids:
  print(f"{hid} is really good at hiding!")

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


# Coins to Cash

def calc_dollars(pennies, nickels, dimes, quarters):

  piggy_bank = {
    "pennies": pennies,
    "nickels": nickels,
    "dimes": dimes,
    "quarters": quarters,
}

  dollar_amount = (piggy_bank["pennies"] / 100) + (piggy_bank["nickels"] / 20) + (piggy_bank["dimes"] / 10) + (piggy_bank["quarters"] / 4)
  print(f"You have {dollar_amount} in change.")

calc_dollars(342, 9, 32, 7)
