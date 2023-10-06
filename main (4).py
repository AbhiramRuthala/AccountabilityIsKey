var = input("What module are you working on? ")

if (var == "Artificial Intelligence"):
  print("That was a while ago. Are you trying to do a focus?")
elif (var == "Synthetic Biology"):
  print("Looks like someone hasn't done their homework. You should ask L'chelle for help if you're confused")
elif (var == "BCIs"):
  print("Brain technology is always very fascinating")
  var4 = input("What card are you working on? ")
  if (int(var4) > 5):
    print("Good work. Continue to do the rest.")
    var3 = input("Do card " + str(int(var4) + 1)+ " of the " + var + " module and post on twitter.") 
    print(var3)
  else:
   print("Might wanna get your work done.")
else: 
  var4 = input("What card are you working on? ")
  if (int(var4) > 5):
    print("Good work. Continue to do the rest.")
    var3 = input("Do card " + str(int(var4) + 1)+ " of the " + var + " module and post on twitter.")
    print(var3)
  else:
    print("Might wanna get your work done.")






#print(var)
#print(var4)
#print(var3)
#print(var2)