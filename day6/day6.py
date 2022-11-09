user = input("Username > ").lower()
passw = input ("Password > ")

if user == "mark" and passw == "password":
  print("Hey Mark, nice to see you again")
elif user == "suzanne" and passw == "wordpass":
  print("Hey Suzanne, welcome back!")
elif user == "rachel" and passw == "S3cur!ty":
  print("Hey Rachel you're really secure")
else:
  print("Womp Womp Womp, you don't belong here")
