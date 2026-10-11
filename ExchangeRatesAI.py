import pandas as pd
class ExchangeRates:
    import pandas as pd


class ExchangeRates:
 def __init__(self, filename):
      # Read the Bank of Canada exchange rate file
         self.data = pd.read_csv(filename)
      # Get the latest USD/CAD exchange rate
         self.rate = self.data["FXAUSDCAD"].iloc[-1]
 
 def convert(self, amount, from_currency, to_currency):
        
        # Convert USD to CAD
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.rate

        # Convert CAD to USD
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.rate

        # No conversion needed
        elif from_currency == to_currency:
            return amount
                    
rates = ExchangeRates("BankOfCanadaExchangeRates.2026.csv")

amount = float(input("Enter amount: "))
from_currency = input("Enter from currency (USD or CAD): ").upper()
to_currency = input("Enter to currency (USD or CAD): ").upper()

result = rates.convert(amount, from_currency, to_currency)

print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")                    