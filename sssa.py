x1 = float(input("enter x1 : "))
y1 = float(input("enter y1 : "))
x1 = round(x1*1000)
x1 = x1/1000
y1 = round(y1*1000)
y1 = y1/1000
if(x1 == y1):
  print("they are the same up to three decimal places")
else:
  print("they arre diferent")