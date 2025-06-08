reply = input()

reply = reply.strip().lower()


if reply == "hello":
  print("$0") 
elif reply[0] == "h":
  print("$20") 
else: 
  print("$100") 
