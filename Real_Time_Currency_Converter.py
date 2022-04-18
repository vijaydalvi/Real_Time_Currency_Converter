from forex_python.converter import CurrencyRates
while True:
    c=CurrencyRates()
    amount=int(input("Enter The Amount:-"))
    from_currency=input("From currency:-").upper()
    to_currency=input("To Currency:-").upper()
    print(from_currency,"To",to_currency,amount)
    result=c.convert(from_currency,to_currency,amount)
    print(result)