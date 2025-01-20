name = input("what the hell is your name: ")
print("Hello " + name + "!")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
  print("play yay, yay!")

  direction = input("Which direction? ").lower()

  if direction == "left":
    print("You went left")
  elif direction == "right":
    print("You went right")
  else:
    print("You went straight")

elif should_we_play == "no":
  print("play nay, nay!")
else:
  print("play whatever you want!")
