# 1 bottle costs 50c
# The machine only accepts these denominations: 25 cents, 10 cents, and 5 cents

amount_due = 50

while amount_due > 0:
  coin = int(input("Insert Coin: "))
  if coin == 25 or coin == 10 or coin == 5:
    amount_due -= coin
  else: 
    pass

if amount_due <= 0:
      print(f"Change Owed:", + amount_due * -1)


# Display amount due
# If > 0, prompt again
# Caluclate change owed in case user added too much