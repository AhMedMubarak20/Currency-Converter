def currency_converter(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

exchange_rate = float(input("Enter exchange rate: "))
amount_in_usd = float(input("Enter amount in USD: "))
converted_amount = currency_converter(amount_in_usd, exchange_rate)
print(f"Equivalent amount in target currency: {converted_amount}")
