year = int(input("Enter the value of a year :"))
if year % 4!= 0:
  print("It's a common year")
elif year %100!= 0:
    print("it's a leap year")
elif year %400 != 0:
    print("It's common year")
else:
    print("It's a leap year")
