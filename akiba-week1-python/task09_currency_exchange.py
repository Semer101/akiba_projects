usd_amount = float(input("Enter amount in USD: "))

exchange_rate = 150 #1 USD = 150 ETB

convert_to_etb = usd_amount * exchange_rate

print("==============================")
print("       CURRENCY EXCHANGE      ")
print("==============================")
print()
print(f"USD Amount: {usd_amount}")
print()
print(f"Exchange Rate: 1 USD = 150 ETB")
print()
print(f"ETB Amount: {convert_to_etb} ETB")
print("==============================")