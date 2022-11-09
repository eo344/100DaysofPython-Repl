q = input("Do you like Gilmore Girls? ")
if q == "yes":
  print("As you should!")
  print("But are you a superfan or a poser?")
  print("I'll ask you a few questions to check \n")
  mainChar = input("Name one Gilmore Girl ").lower()
  if mainChar == "rory" or mainChar == "lorelai" or mainChar == "emily":
    print("Aurkay you know some stuff")
    boy = input("Who was Rory's second boyfriend? ").lower()
    if boy == "jess":
      print("And her best one too, don't care what anyone says")
      print("Okay one final question")
      sister = input("What is Rory's sister's name? ").lower()
      if sister == "gigi":
          print("ding ding ding! you got them all correct you are a real GG Fan")
      else:
        print("Poser!")
    else:
        print("Poser!")
  else:
        print("Poser!")
else:
  print("Loser!")
