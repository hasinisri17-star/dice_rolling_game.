import random
print("Welcome to the dice rolling game!")
while True:
    choice=input("do u want to roll the dice? (y/n): ")
    if choice.lower()=="y":
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f"{die1 } { die2} ,you rolled a {die1+die2}")
      if die1 == die2:
            print("you rolled doubled!")
    elif choice.lower()=="n":
        print("Thank you for comming to the game!")
        break
    else:
        print("invalid value,enter y or n")