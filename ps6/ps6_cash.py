import math

change = int(input("How much change do you need? "))

denominationCoins = 0
totalCoins = 0


if change / 25 != 0: #25c coins
  denominationCoins = math.floor((change / 25))
  totalCoins += denominationCoins
  change = change % 25 

if change / 10 != 0: #10c coins
  denominationCoins = math.floor(change / 10)
  totalCoins += denominationCoins
  change = change % 10

if change / 5 != 0: #5c coins
  denominationCoins = math.floor(change / 5)
  totalCoins += denominationCoins
  change = change % 5

if change > 0: #1c coins
  totalCoins += change

print(totalCoins)