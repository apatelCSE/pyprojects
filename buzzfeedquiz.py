while True:
  print("Tell Us Which of These Movies Made You Cry and We'll Guess Your Favorite Food")
  counter = 0
  titanic = input("Did you cry during Titanic?")
  print(titanic)
  if "y" in titanic:
    counter += 1
  up = input("Did Up make you cry?")
  print(up)
  if "y" in up:
    counter += 1
  notebook = input("Did you cry during The Notebook?")
  print(notebook)
  if "y" in notebook:
    counter += 1
  helps = input("Did The Help make you cry?")
  print(helps)
  if "y" in helps:
    counter += 1  
  insideout = input("Did you cry during Inside Out?")
  print(insideout)
  if "y" in insideout:
    counter += 1
  wonder = input("Did Wonder make you cry?")
  print(wonder)
  if "y" in wonder:
    counter += 1
  if counter <=2:
    print("Your favorite food is cold soup, you heartless scumbag.")
    elif counter <=4:
      print("Your favorite food is mac and cheese.")
    elif counter <=6:
        print("Your favorite food is pizza. Warm and wonderful like your heart! <3")
      break
