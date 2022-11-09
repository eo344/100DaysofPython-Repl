print("""
  CUSTOM AFFIRMATION GENERATOR
              ***
  Hey we're just gonna ask you a few questions
""")

name = input("What's your name? ").lower()
day = input("What's the current day of the week? ").lower()
color = input ("What's your fave colour? ").lower()
flower = input("What's your fave flower? ").lower()

if day == "monday" or day == "wednesday" or day == "friday":
    print("hi", name, "today is", day, "this means today will be filled of", flower, " and", color, "things")
elif day == "tuesday" or day == "thursday":
  print("Hi", name, "today is", day, "this means today will feel", color, "in the best way possible, and I think you're gonna find really pretty", flower, "today")
elif day == "saturday" or day == "sunday":
  print("Hi", name, "Yayyyy it's the weekend, you'll find lot's of", color, " ", flower, "No it's not impossible :)")
else:
  print("Hi", name, "Have a wonderful day!")
