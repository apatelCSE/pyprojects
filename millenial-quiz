while True:
  print("Build a Millenial Lunchbox and We'll Tell You Which Element Best Describes You")
  earth = 0
  air = 0
  water = 0
  fire = 0
  lacroix = input("Choose a flavor of LaCroix: Pure, Berry, Pamplemousse, Pina Fraise Curate, Coconut, Lemon")
  if "pure" in lacroix:
    earth +=1
    air +=3
    water +=2
  elif "berry" in lacroix:
    earth += 3
    water +=1
    fire +=2
  elif "pamp" in lacroix:
    earth +=1
    air += 2
    fire +=3
  elif "pina" in lacroix:
    earth +=3
    water +=1
    fire +=2
  elif "coco" in lacroix:
    earth +=2
    water +=3
    air +=1
  elif "lemon" in lacroix:
    earth +=2
    fire +=1
    air +=3
  rxbar = input("Pick a granola bar flavor: Maple Sea Salt, Chocolate Coconut, Mint Chocolate, Chocolate Chip, Mixed Berry, Peanut Butter Chocolate")
  if "maple" in rxbar:
    earth +=3
    air +=1
    water +=2
  elif "coco" in rxbar:
    earth += 3
    air +=1
    fire +=2
  elif "mint" in rxbar:
    earth +=2
    air += 3
    water +=1
  elif "chip" in rxbar:
    earth +=3
    air +=1
    water +=2
  elif "berry" in rxbar:
    water +=2
    fire +=3
    earth +=1
  elif "peanut" in rxbar:
    earth +=2
    fire +=1
    air +=3
  main = input("Pick a main course: Rainbow Bagel, Ramen Burger, Acai Bowl, Avocado Toast, Sushi Burrito, Artisanal Grilled Cheese")
  if "rainbow" in main:
    fire +=2
    air +=3
    water +=1
  elif "ramen" in main:
    earth += 3
    air +=2
    fire +=1
  elif "acai" in main:
    earth +=2
    air += 3
    water +=1
  elif "avocado" in main:
    earth +=3
    air +=1
    water +=2
  elif "sushi" in main:
    water +=2
    fire +=3
    air +=1
  elif "cheese" in main:
    earth +=2
    fire +=1
    air +=3
  if earth > air and earth > water and earth > fire:
    print("Your element is earth!")
  elif air > earth and air > water and air > fire:
    print("Your element is air!")
  elif fire > earth and fire > water and fire > air:
    print("Your element is fire!")
  elif water > air and water > fire and water > earth:
    print("Your element is water!")
  else:
    print("You're a mix of fire and water!")
  endans = input("Wanna retake the quiz?")
  if "y" in endans:
    continue
  else:
    break
