
print("Crypt ROT-13")
print("By: Eastland Crane")
print()
print("Enter message to be encoded: ")
print("(Spaces will be encoded as well, so leave them out, or put them in as you desire.)")
userinput = input("> ")
print ("Entered message: " + userinput)
abc = "abcdefghijklmnopqrstuvwxyz"
secret = "".join([abc[(abc.find(c)+13)%26] for c in userinput])
print(secret)
