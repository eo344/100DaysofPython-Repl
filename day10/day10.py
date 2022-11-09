myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = float(input("What percentage of tip will you be adding to the bill?"))
myBillTip = (tip/100) * myBill
answer = myBillTip  / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
