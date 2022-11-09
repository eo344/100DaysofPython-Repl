print ("Marvel Movie Character Creator \n --")
s = input("Do you like 'hanging around'?").lower()
if s == 'no' or s == 'n':
  print("Then you're not Spider-man")
  k = input("Do you have a 'gravelly' voice?")
  if k == 'no' or k == 'n':
    print("Aww, then you're not Korg")
    m = input("Do you often feel 'Marvelous'?")
    if m == 'no' or m == 'n':
      a = input("Wow...who are you?")
      print("Oh, hi", a + "!")
    else:
      print("Aha! You're Captain Marvel! Hi!")
  else:
    print("Aha! You're Korg! Hi!")
else:
  print("Aha! You're Spiderman! Hi!")
