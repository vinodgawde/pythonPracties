text=(input("enter value1 = "))
if("money" in text):
   spam = True
elif("gold" in text):
   spam = True
elif("silver" in text):
   spam = True
elif("coin" in text):
   spam = True
else:
   spam = False

if(spam):
  print("this is spam")
else:
  print("this is not spam")